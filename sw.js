const CACHE_NAME = 'nf-care-20261023-v3';
const CACHE_PREFIX = 'nf-care-';
const ASSETS = [
    'index.html',
    'manifest.json',
    'data/study_data.json',
    'icon.svg'
];

self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then((cache) => cache.addAll(ASSETS))
            .then(() => self.skipWaiting())
    );
});

self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys()
            .then((keys) => Promise.all(
                keys.filter((key) => key.startsWith(CACHE_PREFIX) && key !== CACHE_NAME)
                    .map((key) => caches.delete(key))
            ))
            .then(() => self.clients.claim())
    );
});

self.addEventListener('fetch', (event) => {
    if (event.request.method !== 'GET') return;
    const requestUrl = new URL(event.request.url);
    if (requestUrl.origin !== self.location.origin) return;

    event.respondWith(
        caches.open(CACHE_NAME)
            .then((cache) => cache.match(event.request))
            .then((response) => response || fetch(event.request))
    );
});
