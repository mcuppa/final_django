/*!
* Start Bootstrap - Shop Homepage v5.0.6 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

<script>
    document.querySelectorAll('.leer-mas').forEach(function(btn) {
        btn.addEventListener('click', function() {
            var modalId = this.getAttribute('data-target');
            var modal = document.querySelector(modalId);
            var content = modal.querySelector('.modal-body p');
            var fullContent = content.innerHTML;
            var imagenUrl = this.getAttribute('data-imagen');
            var imagen = modal.querySelector('.modal-body img');

            content.innerHTML = fullContent;
            imagen.src = imagenUrl;
        })
    });
</script>

