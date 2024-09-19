/* jshint esversion: 11 */

document.addEventListener('DOMContentLoaded', function() {
    // dynamically change the hero-image background depending on page (home or about)
    const heroImageHome = document.getElementById('hero-image');
    if (heroImageHome) {
        const imageUrlHome = heroImageHome.getAttribute('data-image-url');
        heroImageHome.style.backgroundImage = `url("${imageUrlHome}")`;
    }

    const heroImageAbout = document.getElementById('about-image');
    if (heroImageAbout) {
        const imageUrlAbout = heroImageAbout.getAttribute('data-image-url');
        heroImageAbout.style.backgroundImage = `url("${imageUrlAbout}")`;
    }

    // add `<br>` on forms before "comments" `<textarea>`
    const commentsLabel = document.querySelector('label[for="id_comments"]');
    if (commentsLabel) {
        const lineBreak = document.createElement('br');
        commentsLabel.parentNode.insertBefore(lineBreak, commentsLabel.nextSibling);
    }

    // set all `date` input fields to have a maximum date of "today", no future DOBs
    document.querySelectorAll('input[type="date"]').forEach(input => {
        const today = new Date().toISOString().split("T")[0];
        input.setAttribute("max", today);
    });
});

document.addEventListener('DOMContentLoaded', function() {
    var deleteModal = document.getElementById('deleteConfirmModal');
    var confirmDeleteBtn = document.getElementById('confirmDelete');
    var formToSubmit;

    deleteModal.addEventListener('show.bs.modal', function (event) {
        var button = event.relatedTarget;
        formToSubmit = button.closest('form');
    });

    confirmDeleteBtn.addEventListener('click', function() {
        formToSubmit.submit();
    });
});