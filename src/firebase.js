import { initializeApp } from 'firebase/app';
import { 
  getFirestore, 
  collection, 
  addDoc, 
  query, 
  orderBy, 
  onSnapshot, 
  getDocs,
  serverTimestamp 
} from 'firebase/firestore';

// Firebase configuration - Arief & Syifa Wedding 2026
const firebaseConfig = {
  apiKey: "AIzaSyCJrZeuSk5nq-fghGIi2N_TlCgLeuvz0Ko",
  authDomain: "undangan-arief-syifa.firebaseapp.com",
  projectId: "undangan-arief-syifa",
  storageBucket: "undangan-arief-syifa.firebasestorage.app",
  messagingSenderId: "101215900603",
  appId: "1:101215900603:web:334569084d96a68b886a9e",
  measurementId: "G-3X4Z7H6B3Q"
};

// Check if Firebase configurations are available
const isFirebaseConfigured = !!firebaseConfig.projectId;

let app = null;
let db = null;

if (isFirebaseConfigured) {
  try {
    app = initializeApp(firebaseConfig);
    db = getFirestore(app);
    console.log("Firebase Firestore successfully initialized.");
  } catch (error) {
    console.error("Failed to initialize Firebase:", error);
  }
} else {
  console.warn("Firebase configuration is missing (VITE_FIREBASE_PROJECT_ID). Falling back to LocalStorage.");
}

// LocalStorage Event Bus for Offline Realtime Updates
const localWishCallbacks = new Set();
const triggerLocalWishesUpdate = () => {
  const wishes = getLocalWishes();
  localWishCallbacks.forEach(callback => callback(wishes));
};

// LocalStorage Helper functions
const getLocalWishes = () => {
  try {
    const wishes = localStorage.getItem('wedding_wishes');
    return wishes ? JSON.parse(wishes) : getMockWishes();
  } catch (e) {
    return getMockWishes();
  }
};

const saveLocalWish = (wish) => {
  const wishes = getLocalWishes();
  wishes.unshift(wish); // Prepend to show newest first
  localStorage.setItem('wedding_wishes', JSON.stringify(wishes));
  triggerLocalWishesUpdate();
};

const getLocalRSVPs = () => {
  try {
    const rsvps = localStorage.getItem('wedding_rsvps');
    return rsvps ? JSON.parse(rsvps) : [];
  } catch (e) {
    return [];
  }
};

const saveLocalRSVP = (rsvp) => {
  const rsvps = getLocalRSVPs();
  rsvps.push(rsvp);
  localStorage.setItem('wedding_rsvps', JSON.stringify(rsvps));
};

// Helper mock wishes for visual excellence on first load
function getMockWishes() {
  return [
    {
      id: 'mock-1',
      name: 'Rian & Dini',
      attendance: 'Hadir',
      message: 'Selamat ya Arief & Syifa! Semoga menjadi keluarga yang sakinah, mawaddah, warahmah. Maaf belum bisa hadir langsung, tapi doa kami menyertai kalian.',
      timestamp: new Date(Date.now() - 1000 * 60 * 30).toISOString() // 30 mins ago
    },
    {
      id: 'mock-2',
      name: 'Siti Rahmawati',
      attendance: 'Hadir',
      message: 'MasyaAllah cantik dan ganteng banget! Selamat menempuh hidup baru kalian berdua, semoga dilancarkan segala urusannya dan cepat dikaruniai momongan.',
      timestamp: new Date(Date.now() - 1000 * 60 * 120).toISOString() // 2 hours ago
    },
    {
      id: 'mock-3',
      name: 'Budi Santoso',
      attendance: 'Tidak Hadir',
      message: 'Selamat menempuh bahtera rumah tangga baru. Semoga berkah berlimpah untuk Arief dan Syifa selamanya. Amin!',
      timestamp: new Date(Date.now() - 1000 * 60 * 300).toISOString() // 5 hours ago
    }
  ];
}

/**
 * Submits an RSVP and Wish
 * @param {Object} data - { name, guests, attendance, message }
 */
export async function submitRSVPApi(data) {
  const wishData = {
    name: data.name,
    attendance: data.attendance,
    message: data.message || '',
    timestamp: new Date().toISOString()
  };

  if (isFirebaseConfigured && db) {
    try {
      // 1. Save RSVP
      await addDoc(collection(db, 'rsvps'), {
        ...data,
        timestamp: serverTimestamp()
      });

      // 2. If guest writes a message, save it to wishes collection
      if (wishData.message.trim()) {
        await addDoc(collection(db, 'wishes'), {
          ...wishData,
          timestamp: serverTimestamp()
        });
      }
      return { success: true };
    } catch (error) {
      console.error("Firebase submit error, falling back to LocalStorage:", error);
      // Fallback on error
      saveLocalRSVP(data);
      if (wishData.message.trim()) {
        saveLocalWish(wishData);
      }
      return { success: true, fallback: true };
    }
  } else {
    // LocalStorage Fallback
    saveLocalRSVP(data);
    if (wishData.message.trim()) {
      saveLocalWish(wishData);
    }
    // Artificial small delay for realistic UX
    await new Promise(resolve => setTimeout(resolve, 800));
    return { success: true, fallback: true };
  }
}

/**
 * Subscribes to real-time wishes updates
 * @param {Function} callback - Callback function receives list of wishes
 * @returns {Function} Unsubscribe function
 */
export function subscribeToWishes(callback) {
  if (isFirebaseConfigured && db) {
    const wishesQuery = query(collection(db, 'wishes'), orderBy('timestamp', 'desc'));
    
    return onSnapshot(wishesQuery, (snapshot) => {
      const wishes = [];
      snapshot.forEach((doc) => {
        const data = doc.data();
        let timestampStr = new Date().toISOString();
        if (data.timestamp) {
          // Firebase Timestamp might be null briefly on local cache write
          timestampStr = typeof data.timestamp.toDate === 'function' 
            ? data.timestamp.toDate().toISOString() 
            : new Date(data.timestamp).toISOString();
        }
        wishes.push({
          id: doc.id,
          ...data,
          timestamp: timestampStr
        });
      });
      callback(wishes.length > 0 ? wishes : getMockWishes());
    }, (error) => {
      console.error("Firestore onSnapshot error, using LocalStorage updates:", error);
      // Fallback subscribe
      localWishCallbacks.add(callback);
      callback(getLocalWishes());
    });
  } else {
    // LocalStorage Fallback subscribe
    localWishCallbacks.add(callback);
    // Send initial data immediately
    callback(getLocalWishes());
    
    // Return unsubscribe function
    return () => {
      localWishCallbacks.delete(callback);
    };
  }
}
