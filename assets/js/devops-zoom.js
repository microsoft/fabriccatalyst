// Lightweight zoom in/out for images with class 'zoomable-devops'
document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('img.zoomable-devops').forEach(function (img) {
        img.style.cursor = 'zoom-in';
        img.addEventListener('click', function () {
            if (!img.classList.contains('zoomed')) {
                img.classList.add('zoomed');
                img.style.cursor = 'zoom-out';
                document.body.style.overflow = 'hidden';
            } else {
                img.classList.remove('zoomed');
                img.style.cursor = 'zoom-in';
                document.body.style.overflow = '';
            }
        });
    });
}); 