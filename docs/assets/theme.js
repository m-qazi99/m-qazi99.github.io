/* Apply a saved light palette before the first paint. */
'use strict';
(()=>{const allowed=['champagne','pearl','aurora','rose'];let theme='champagne';try{const saved=localStorage.getItem('mq-color-theme');if(allowed.includes(saved))theme=saved;}catch{}document.documentElement.dataset.theme=theme;})();
