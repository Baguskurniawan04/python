<!DOCTYPE html>
<html lang="en">
<head>
<title>GALERI</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<link href="https://fonts.googleapis.com/css?family=Quicksand:300,400,500,700,900" rel="stylesheet">
<link rel="stylesheet" href="https://colorlib.com/preview/theme/shutter/fonts/icomoon/style.css">
<link rel="stylesheet" href="https://colorlib.com/preview/theme/shutter/css/bootstrap.min.css">
<link rel="stylesheet" href="https://colorlib.com/preview/theme/shutter/css/magnific-popup.css">
<link rel="stylesheet" href="https://colorlib.com/preview/theme/shutter/css/jquery-ui.css">
<link rel="stylesheet" href="https://colorlib.com/preview/theme/shutter/css/owl.carousel.min.css">
<link rel="stylesheet" href="https://colorlib.com/preview/theme/shutter/css/owl.theme.default.min.css">
<link rel="stylesheet" href="https://colorlib.com/preview/theme/shutter/css/bootstrap-datepicker.css">
<link rel="stylesheet" href="https://colorlib.com/preview/theme/shutter/fonts/flaticon/font/flaticon.css">
<link rel="stylesheet" href="https://colorlib.com/preview/theme/shutter/css/aos.css">
<link rel="stylesheet" href="https://colorlib.com/preview/theme/shutter/css/fancybox.min.css">
<link rel="stylesheet" href="https://colorlib.com/preview/theme/shutter/css/style.css">
</head>
<body>
<div class="site-wrap">
<div class="site-mobile-menu">
<div class="site-mobile-menu-header">
<div class="site-mobile-menu-close mt-3">
<span class="icon-close2 js-menu-toggle"></span>
</div>
</div>
<div class="site-mobile-menu-body"></div>
</div>
<header class="header-bar d-flex d-lg-block align-items-center" data-aos="fade-left">
<div class="site-logo">
<a href="index.html">GALERI</a>
</div>
<div class="d-inline-block d-xl-none ml-md-0 ml-auto py-3" style="position: relative; top: 3px;"><a href="#" class="site-menu-toggle js-menu-toggle text-white"><span class="icon-menu h3"></span></a></div>
<div class="main-menu">
<ul class="js-clone-nav">
<li class="active"><a href="http://bagus01.pythonanywhere.com/">Upload File</a></li>
</ul>
</div>
</header>
<main class="main-content">
<div class="container-fluid photos">
<div class="row align-items-stretch mt-3">

{% for image_name in image_names %}
<div class="col-12 col-md-6 col-lg-6" data-aos="fade-up">
<a href="{{url_for('send_image', filename=image_name)}}" target="_blank" class="d-block photo-item">
<img src="{{url_for('send_image', filename=image_name)}}" alt="Image" class="img-fluid">
<div class="photo-text-more">
<div class="photo-text-more">
<h3 class="heading">{{image_name}}</h3>
<span class="meta">SHOW IMAGE IN NEW TAB</span>
</div>
</div>
</a>
</div>
{% endfor %}

</div>
<div class="row justify-content-center">
<div class="col-md-12 text-center py-5">
<p>

Terimakasih Untuk Colorlib Untuk Templatenya ^_^

</p>
</div>
</div>
</div>
</main>
</div>
<script src="https://colorlib.com/preview/theme/shutter/js/jquery-3.3.1.min.js" type="2042aa76633a895ae01700c5-text/javascript"></script>
<script src="https://colorlib.com/preview/theme/shutter/js/jquery-migrate-3.0.1.min.js" type="2042aa76633a895ae01700c5-text/javascript"></script>
<script src="https://colorlib.com/preview/theme/shutter/js/jquery-ui.js" type="2042aa76633a895ae01700c5-text/javascript"></script>
<script src="https://colorlib.com/preview/theme/shutter/js/popper.min.js" type="2042aa76633a895ae01700c5-text/javascript"></script>
<script src="https://colorlib.com/preview/theme/shutter/js/bootstrap.min.js" type="2042aa76633a895ae01700c5-text/javascript"></script>
<script src="https://colorlib.com/preview/theme/shutter/js/owl.carousel.min.js" type="2042aa76633a895ae01700c5-text/javascript"></script>
<script src="https://colorlib.com/preview/theme/shutter/js/jquery.stellar.min.js" type="2042aa76633a895ae01700c5-text/javascript"></script>
<script src="https://colorlib.com/preview/theme/shutter/js/jquery.countdown.min.js" type="2042aa76633a895ae01700c5-text/javascript"></script>
<script src="https://colorlib.com/preview/theme/shutter/js/jquery.magnific-popup.min.js" type="2042aa76633a895ae01700c5-text/javascript"></script>
<script src="https://colorlib.com/preview/theme/shutter/js/bootstrap-datepicker.min.js" type="2042aa76633a895ae01700c5-text/javascript"></script>
<script src="https://colorlib.com/preview/theme/shutter/js/aos.js" type="2042aa76633a895ae01700c5-text/javascript"></script>
<script src="https://colorlib.com/preview/theme/shutter/js/jquery.fancybox.min.js" type="2042aa76633a895ae01700c5-text/javascript"></script>
<script src="https://colorlib.com/preview/theme/shutter/js/main.js" type="2042aa76633a895ae01700c5-text/javascript"></script>
<script src="https://ajax.cloudflare.com/cdn-cgi/scripts/7089c43e/cloudflare-static/rocket-loader.min.js" data-cf-settings="2042aa76633a895ae01700c5-|49" defer=""></script></body>
</html>
