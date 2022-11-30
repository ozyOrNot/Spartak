// Получаю все элементы с классом popup-link
// const popupLinks = document.querySelectorAll('.popup-link');
// Получаю тело страницы (нужно для блокировки скролла)
// const body = document.querySelector('body');
// const lockPadding = document.querySelectorAll(".lock-padding")

// let unlock = false

// Время задержки
// const timeout = 600;

// if (popupLinks.length > 0) {
//     for (let index = 0; index < popupLinks.length; index++) {
//         const popupLink = popupLinks[index];
//         popupLink.addEventListener("click", function (e) {
//             const popupName = popupLink.getAttribute('href').replace('#', '');
//             const curentPopup = document.getElementById(popupName);
//             popupOpen(curentPopup);
//             e.preventDefault();
//         });
//     }
// }

// function popupOpen(curentPopup) {
//     if (curentPopup && unlock) {
//         const popupActive = document.querySelector('.popup.open');
//         if (popupActive) {
//             popupClose(popupActive, false);
//         } else {
//             bodyLock();
//         }

//         curentPopup.classList.add('open');
//         curentPopup.addEventListener("click", function (e) {
//             if (!e.target.closest('.popup__content')) {
//                 popupClose(e.target.closest('.popup'))
//             }
//         });
//     }
// }

// const popupCloseIcon = document.querySelectorAll('.close-popup');
// if (popupCloseIcon.length > 0) {
//     for (let index = 0; index < popupCloseIcon.length; index++) {
//         const el = popupCloseIcon[index];
//         el.addEventListener("click", function (e) {
//             popupClose(el.closest('.popup'));
//             e.preventDefault();
//         });
//     }
// }


// function popupClose(popupActive, doUnlock=true) {
//     if (unlock) {
//         popupActive.classList.remove('open');
//         if (doUnlock) {
//             bodyLock();
//         }
//     }
// }

// function bodyLock() {
//     const lockPaddingValue = window.innerWidth - document.querySelector('.main__body').offsetWidth + 'px';

//     for (let index = 0; index < lockPadding.length; index++) {
//         const el = lockPadding[index];
//         el.style.paddingRight = lockPaddingValue;
//     }
// }

