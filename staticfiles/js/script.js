document.addEventListener('DOMContentLoaded', function() {
        var heroImage = document.getElementById('hero-image');
        var imageUrl = heroImage.getAttribute('data-image-url');
        heroImage.style.backgroundImage = 'url("' + imageUrl + '")';
    });


    document.addEventListener('DOMContentLoaded', function() {
        var heroImage = document.getElementById('about-image');
        var imageUrl = heroImage.getAttribute('data-image-url');
        heroImage.style.backgroundImage = 'url("' + imageUrl + '")';
    });

    document.addEventListener('DOMContentLoaded', function() {
        const commentsLabel = document.querySelector('label[for="id_comments"]');
        if (commentsLabel) {
            const lineBreak = document.createElement('br');
            commentsLabel.parentNode.insertBefore(lineBreak, commentsLabel.nextSibling);
        }
    });