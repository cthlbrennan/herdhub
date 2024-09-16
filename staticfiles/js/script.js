document.addEventListener('DOMContentLoaded', function() {
        var heroImage = document.getElementById('hero-image');
        var imageUrl = heroImage.getAttribute('data-image-url');
        heroImage.style.backgroundImage = 'url("' + imageUrl + '")';
    });
