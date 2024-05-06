// Function to disable tab focus
function disableTabFocus() {
    const handles = document.getElementsByClassName('rc-slider-handle');
    for (let i = 0; i < handles.length; i++) {
        handles[i].setAttribute('tabindex', '-1');
    }
}
// Create a MutationObserver
const observer = new MutationObserver(disableTabFocus);

// Set up the observer to watch for changes in the body
observer.observe(document.body, { childList: true, subtree: true });

// Ensure the modification runs on initial load
disableTabFocus();
