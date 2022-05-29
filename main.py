import argparse
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory

app = Flask(__name__)


def start():
    put_grid([[None,None,None,None,put_html('''<html lang="en" class="link-html"><head>
        <title>MoiCbio</title>
        <base href="https://app.znaplink.com/">
        <meta http-equiv="content-type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

                <meta property="og:site_name" content="Znaplink">
        <meta property="og:title" content="MoiCbio">
        <meta property="og:description" content="we're just still running  // welcome">
        <meta property="og:image" content="https://app.znaplink.com/uploads/avatars/https://imagedelivery.net/tqC70bVt8T6GtQUXNsa2-g/6c636793-678b-4e46-dc8b-cc2ca58dde00/public">
        <meta property="og:url" content="https://znap.link/MoiCbio">

        
        <meta name="twitter:title" content="MoiCbio">
        <meta name="twitter:description" content="we're just still running  // welcome">
        <meta name="twitter:image" content="https://app.znaplink.com/uploads/avatars/https://imagedelivery.net/tqC70bVt8T6GtQUXNsa2-g/6c636793-678b-4e46-dc8b-cc2ca58dde00/public">
        <meta name="twitter:card" content="summary_large_image">
        
                    <!-- Open Graph / Facebook -->
                                                <!-- <meta property="og:" content="" /> -->
                                    
                    <!-- Twitter -->
                                                <meta property="twitter:type" content="website">
                                                                <meta property="twitter:url" content="https://znap.link/MoiCbio">
                                                                                                                        
                    <meta name="robots" content="noindex">
        
                    <style type="text/css">svg:not(:root).svg-inline--fa{overflow:visible}.svg-inline--fa{display:inline-block;font-size:inherit;height:1em;overflow:visible;vertical-align:-.125em}.svg-inline--fa.fa-lg{vertical-align:-.225em}.svg-inline--fa.fa-w-1{width:.0625em}.svg-inline--fa.fa-w-2{width:.125em}.svg-inline--fa.fa-w-3{width:.1875em}.svg-inline--fa.fa-w-4{width:.25em}.svg-inline--fa.fa-w-5{width:.3125em}.svg-inline--fa.fa-w-6{width:.375em}.svg-inline--fa.fa-w-7{width:.4375em}.svg-inline--fa.fa-w-8{width:.5em}.svg-inline--fa.fa-w-9{width:.5625em}.svg-inline--fa.fa-w-10{width:.625em}.svg-inline--fa.fa-w-11{width:.6875em}.svg-inline--fa.fa-w-12{width:.75em}.svg-inline--fa.fa-w-13{width:.8125em}.svg-inline--fa.fa-w-14{width:.875em}.svg-inline--fa.fa-w-15{width:.9375em}.svg-inline--fa.fa-w-16{width:1em}.svg-inline--fa.fa-w-17{width:1.0625em}.svg-inline--fa.fa-w-18{width:1.125em}.svg-inline--fa.fa-w-19{width:1.1875em}.svg-inline--fa.fa-w-20{width:1.25em}.svg-inline--fa.fa-pull-left{margin-right:.3em;width:auto}.svg-inline--fa.fa-pull-right{margin-left:.3em;width:auto}.svg-inline--fa.fa-border{height:1.5em}.svg-inline--fa.fa-li{width:2em}.svg-inline--fa.fa-fw{width:1.25em}.fa-layers svg.svg-inline--fa{bottom:0;left:0;margin:auto;position:absolute;right:0;top:0}.fa-layers{display:inline-block;height:1em;position:relative;text-align:center;vertical-align:-.125em;width:1em}.fa-layers svg.svg-inline--fa{-webkit-transform-origin:center center;transform-origin:center center}.fa-layers-counter,.fa-layers-text{display:inline-block;position:absolute;text-align:center}.fa-layers-text{left:50%;top:50%;-webkit-transform:translate(-50%,-50%);transform:translate(-50%,-50%);-webkit-transform-origin:center center;transform-origin:center center}.fa-layers-counter{background-color:#ff253a;border-radius:1em;-webkit-box-sizing:border-box;box-sizing:border-box;color:#fff;height:1.5em;line-height:1;max-width:5em;min-width:1.5em;overflow:hidden;padding:.25em;right:0;text-overflow:ellipsis;top:0;-webkit-transform:scale(.25);transform:scale(.25);-webkit-transform-origin:top right;transform-origin:top right}.fa-layers-bottom-right{bottom:0;right:0;top:auto;-webkit-transform:scale(.25);transform:scale(.25);-webkit-transform-origin:bottom right;transform-origin:bottom right}.fa-layers-bottom-left{bottom:0;left:0;right:auto;top:auto;-webkit-transform:scale(.25);transform:scale(.25);-webkit-transform-origin:bottom left;transform-origin:bottom left}.fa-layers-top-right{right:0;top:0;-webkit-transform:scale(.25);transform:scale(.25);-webkit-transform-origin:top right;transform-origin:top right}.fa-layers-top-left{left:0;right:auto;top:0;-webkit-transform:scale(.25);transform:scale(.25);-webkit-transform-origin:top left;transform-origin:top left}.fa-lg{font-size:1.3333333333em;line-height:.75em;vertical-align:-.0667em}.fa-xs{font-size:.75em}.fa-sm{font-size:.875em}.fa-1x{font-size:1em}.fa-2x{font-size:2em}.fa-3x{font-size:3em}.fa-4x{font-size:4em}.fa-5x{font-size:5em}.fa-6x{font-size:6em}.fa-7x{font-size:7em}.fa-8x{font-size:8em}.fa-9x{font-size:9em}.fa-10x{font-size:10em}.fa-fw{text-align:center;width:1.25em}.fa-ul{list-style-type:none;margin-left:2.5em;padding-left:0}.fa-ul>li{position:relative}.fa-li{left:-2em;position:absolute;text-align:center;width:2em;line-height:inherit}.fa-border{border:solid .08em #eee;border-radius:.1em;padding:.2em .25em .15em}.fa-pull-left{float:left}.fa-pull-right{float:right}.fa.fa-pull-left,.fab.fa-pull-left,.fal.fa-pull-left,.far.fa-pull-left,.fas.fa-pull-left{margin-right:.3em}.fa.fa-pull-right,.fab.fa-pull-right,.fal.fa-pull-right,.far.fa-pull-right,.fas.fa-pull-right{margin-left:.3em}.fa-spin{-webkit-animation:fa-spin 2s infinite linear;animation:fa-spin 2s infinite linear}.fa-pulse{-webkit-animation:fa-spin 1s infinite steps(8);animation:fa-spin 1s infinite steps(8)}@-webkit-keyframes fa-spin{0%{-webkit-transform:rotate(0);transform:rotate(0)}100%{-webkit-transform:rotate(360deg);transform:rotate(360deg)}}@keyframes fa-spin{0%{-webkit-transform:rotate(0);transform:rotate(0)}100%{-webkit-transform:rotate(360deg);transform:rotate(360deg)}}.fa-rotate-90{-webkit-transform:rotate(90deg);transform:rotate(90deg)}.fa-rotate-180{-webkit-transform:rotate(180deg);transform:rotate(180deg)}.fa-rotate-270{-webkit-transform:rotate(270deg);transform:rotate(270deg)}.fa-flip-horizontal{-webkit-transform:scale(-1,1);transform:scale(-1,1)}.fa-flip-vertical{-webkit-transform:scale(1,-1);transform:scale(1,-1)}.fa-flip-both,.fa-flip-horizontal.fa-flip-vertical{-webkit-transform:scale(-1,-1);transform:scale(-1,-1)}:root .fa-flip-both,:root .fa-flip-horizontal,:root .fa-flip-vertical,:root .fa-rotate-180,:root .fa-rotate-270,:root .fa-rotate-90{-webkit-filter:none;filter:none}.fa-stack{display:inline-block;height:2em;position:relative;width:2.5em}.fa-stack-1x,.fa-stack-2x{bottom:0;left:0;margin:auto;position:absolute;right:0;top:0}.svg-inline--fa.fa-stack-1x{height:1em;width:1.25em}.svg-inline--fa.fa-stack-2x{height:2em;width:2.5em}.fa-inverse{color:#fff}.sr-only{border:0;clip:rect(0,0,0,0);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;width:1px}.sr-only-focusable:active,.sr-only-focusable:focus{clip:auto;height:auto;margin:0;overflow:visible;position:static;width:auto}.svg-inline--fa .fa-primary{fill:var(--fa-primary-color,currentColor);opacity:1;opacity:var(--fa-primary-opacity,1)}.svg-inline--fa .fa-secondary{fill:var(--fa-secondary-color,currentColor);opacity:.4;opacity:var(--fa-secondary-opacity,.4)}.svg-inline--fa.fa-swap-opacity .fa-primary{opacity:.4;opacity:var(--fa-secondary-opacity,.4)}.svg-inline--fa.fa-swap-opacity .fa-secondary{opacity:1;opacity:var(--fa-primary-opacity,1)}.svg-inline--fa mask .fa-primary,.svg-inline--fa mask .fa-secondary{fill:#000}.fad.fa-inverse{color:#fff}</style><link href="https://app.znaplink.com/uploads/favicon/f5bca4b8ab78370ee3bda11ff8bef797.png" rel="shortcut icon">
        
        
                    <link href="https://app.znaplink.com/themes/altum/assets/css/bootstrap.min.css?v=2&amp;init=1653850234" rel="stylesheet" media="screen">
                    <link href="https://app.znaplink.com/themes/altum/assets/css/custom.css?v=2&amp;init=1653850234" rel="stylesheet" media="screen">
                    <link href="https://app.znaplink.com/themes/altum/assets/css/link-custom.css?v=2&amp;init=1653850234" rel="stylesheet" media="screen">
                    <link href="https://app.znaplink.com/themes/altum/assets/css/animate.min.css?v=2&amp;init=1653850234" rel="stylesheet" media="screen">
        
                                <link href="https://fonts.googleapis.com/css?family=Lato&amp;display=swap" rel="stylesheet">
            <style>
                body {
                    font-family: 'Lato', sans-serif !important;
                }
            </style>
        
        
        
        <link rel="canonical" href="https://znap.link/MoiCbio">
        <style>
            html{
                    background-color: white !important;
                }
                @media(min-width:993px){
                    .single-link-block-img{
                        width:30%;
                    }
                    .container.animate__animated.animate__fadeIn,.profile_description div{
                        max-width: 900px !important;
                        margin:0 auto !important;
                        /* text-align:center; */
                    }
                }
        </style>
    <style>
   /* @font-face {
   font-family: "Circular Std Book"; 
   src: url("/themes/altum/assets/fonts/circular-medium.otf") format("opentype"), 
   url("/themes/altum/assets/fonts/circular-medium-italic.otf") format("opentype"), 
   url("/themes/altum/assets/fonts/circular-bold.otf") format("opentype"), 
   url("/themes/altum/assets/fonts/circular-black.otf") format("opentype"); 
   }
   * {
   font-family: "Circular Std Book";
   } */
   html{
                    background-color: white !important;
                }
                @media(min-width:993px){
                    .single-link-block-img{
                        width:30%;
                    }
                    .container.animate__animated.animate__fadeIn,.profile_title,.profile_description div,.profile_socials{
                        max-width: 900px !important;
                        margin:0 auto !important;
                        /* text-align:center; */
                    }
                }
   
        
          
         
          .single-link-block{
              background-color: #5d23db !important;
              box-shadow: 0px 0px 15px rgb(17 21 26 / 40%);
          }
          
  
   
   
   }
   .profile-main.animate__animated.animate__fadeIn{
   background-color:#5d23db !important;
   padding: 30px 0;
      
   }
   .profile-main{
   width:100%;
   padding:50px 0;
   /* border-bottom:2px solid #f3f3f3; */
   /* max-width:1400px !important; */
   }
   .profile-img-div{
   /* height:100px; */
   text-align:center !important; 
   /* background-color:red; */
   /* justify-content:flex-end; */
   display:flex; 
   }
   .profile-info-div{
   /* height:100px; */
   text-align:center !important; 
   align-items:start;
   margin-bottom:-1px;
   /* background-color:red; */
   }
   .profile-info-div h2{
   font-weight:600;
   letter-spacing:-1px;
   }
   .profile-info-div small{
   font-size:14px;
   width:100%;
   }
   .profile-info-div h2,.profile-info-div p,.profile-info-div small{
   width:100%;
   /* float:left; */
   text-align:left;
   margin:0;
   }
   .profile-info-div p{
   margin:10px 0;  
   }
   .container{
   max-width:1300px;
   }
   .user-avatar{
   margin:0 !important;
   max-width:150px;
   max-height:150px;
   width:120px;
   height:120px;
   }
   .link-card{
   width: 275px;
   height: 260px;
   padding: 10px 10px;
   padding-left: 5px;
   margin:0;
   }
   .link-card a{
   border-radius:40px;
   padding:16px;
   min-height: 360px;
   max-height: 360px;
   }
   /* .link-card-single{
   max-height:550px !important;
   min-height:450px !important;
   } */
   @media(max-width:400px){
   /* .link-card-single{
   min-height:400px !important;
   } */
   }
   .link-card-single div:first-child,.link-card-single div:first-child a{
   height:100%;
   min-height: inherit;
   }
   .link-card-single div:first-child a{
   max-height:fit-content !important;
   }
   .link-img-div{
   width:100%;
   /* height:151px; */
   background-color:#212930;
   border-radius:25px;
   display:flex;
   align-items:center;
   justify-content:center;
   overflow:hidden;
   }
   .link-img-div img{
   /* width:70px;
   height:70px; */
   width:100%;
   min-height: 100%;
   }
   .link-title{
   font-size:22px;
   margin:15px 0;
   font-weight:600;
   text-align:left;
   margin-bottom:7px;
   }
   .link-description{
   margin-top: 0;
   margin-bottom: 0;
   color: #404762;
   font-size: 15px;
   line-height: 20px;
   text-align:left;
   font-weight:400;
   }
   .social-links-div{
   /* background-color: #f3f3f3;
   border-radius: 50%; */
   padding: 5px;
   display: inline-flex;
   -webkit-animation: in 1s;
   /* margin-right:2px; */
   }
   .social-links-div .fa-2x{
   font-size:21px;
   }
   .social-links-div:hover{
   transform: scale(1.2);
   -webkit-transform: scale(1.2);
   -moz-transform: scale(1.2);
   -o-transform: scale(1.2);
   -ms-transform: scale(1.2);
   }
   .slick-track{ margin-left: 0 !important; }
   .div-block-342 {
   display: -webkit-box;
   display: -webkit-flex;
   display: -ms-flexbox;
   display: flex;
   width: 90%;
   margin-top: 0;
   padding-top: 10px;
   padding-bottom: 10px;
   -webkit-box-pack: center;
   -webkit-justify-content: center;
   -ms-flex-pack: center;
   justify-content: center;
   -webkit-box-align: center;
   -webkit-align-items: center;
   -ms-flex-align: center;
   align-items: center;
   border-radius: 50px;
   background-color:#212930;
   position: absolute;
   bottom: 18px;
   white-space: nowrap;
   overflow: hidden;
   text-overflow: ellipsis;
   font-size: 14px;
   font-weight: 600;
   left: 5%;
   }
   .font-weight-medium2{
   font-weight:600;
   }
   .profile-img-div{
   justify-content:center;
   }
   .profile-info-div h2, .profile-info-div p, .profile-info-div small{
   text-align:center;
   }
   .slick-list{padding:0 21% 0 5% !important;}
   @media(max-width:767px){
   .user-avatar{
   width:100px;
   height:100px;
   }
   .profile-main{
   padding:25px 0;
   }
   }
   @media(max-width:550px){
   footer{
   height:auto;
   }
   }
   @media(max-width:500px){
   }
   @media(max-width:400px){
   .link-img-div{
   /* height:150px; */
   }
   }
   .slick-track
   {
   display: flex !important;
   }
   .slick-slide
   {
   height: inherit !important;
   }
   /* .link-card{
   flex-basis:25%;
   } */
   .links-slider{
   flex-basis:100%;
   padding-left: 10px;
   padding-right: 10px;
   /* padding-bottom:20px; */
   padding-bottom: 10px;
   padding-top: 10px;
   }
   .links-slider-main{
   /* margin-left:0;
   padding-left:5px; */
   margin-bottom:10px;
   }
   /* .tiktok-links-slider-main{
        width:120% !important;
        margin-left:0%;
    }
   .tiktok-links-slider-main div div{
       width:250px;
   } */
   @media(max-width:1200px){

    /* .tiktok-links-slider-main{
        width:100% !important;
        margin-left:0%;
    } */
   }
   ._embed_video_wrapper{
       border: none !important;
   }
   .links-slider-main::-webkit-scrollbar {
   height:0.5em;
   }
   .links-slider-main::-webkit-scrollbar-track {
   }
   .links-slider-main::-webkit-scrollbar-thumb {
   background-color: #d3d3d3;
   border-radius:50px;
   }
   @media(min-width:767px){
   .links-slider{
   flex-wrap:wrap;
   display:flex;
   align-items:center;
   margin:0;
   }
   .tiktok-links-slider-main .links-slider{
       justify-content:center;
   }
   .link-card{
   flex-basis:33%;
   height:auto;
   }
   }
   /* for 16:9 img */
   @media(max-width:1200px){
   .link-img-div{
   /* height:137px; */
   }
   }
   @media(max-width:1000px){
   .link-img-div{
   /* height:109px; */
   }
   .link-card{
   flex-basis:33%;
   height:auto;
   }
   .link-card-single{
   flex-basis:33%;
   height: inherit;
   }
   }
   @media(max-width:767px){
   .link-card{
   flex-basis:auto;
   /* height:auto; */
   }
   .profile_description{
   font-size:15px;
   }
   .link-content{
   padding:0rem 1rem;
   }
   .links-slider-main{
   overflow-x:scroll;
   }
   .links-slider{
   display:flex;
   }
   .folder-title{
   text-align:left !important;   
   }
   }
   .profile_description{
   font-size: 15px;
   font-weight:500;
   }
   .profile_description,.link-description,.social-links-div,.single-link-block-details p,.widget-block p{
   color: #fff !important;
   }
   .social-links-div svg path{
   fill: #fff !important;
   }
   .profile_title,.link-title,.folder-title,.single-link-block-details h4,.single-link-block-details h4, .text-block-main h4, .text-block-main h1, .text-block-main p,.widget-block h4{
   color: #fff !important;
    }
    .text-block-divider{
        background: #fff !important;
    }
 
   
   .folder-title{
   font-size:22px;
   text-align:center;
   }
   .btn-primary:focus, .btn-primary.focus{
   box-shadow: 0px 0px 15px #00008024 !important;
   }
   .div-block-342{
   color: #fff   }
   .profile_title{
   overflow-wrap: anywhere;
   }
   .single-link-block-img,.widget-block{
   background-color:#212930;
   }
   input{
   background-color: white !important;
   border-radius:30px !important;
   padding:12px !important;
   }
      
    .profile-main.animate__animated.animate__fadeIn{
        padding-bottom:0 !important;

    }
    .profile_banner_main{
            }
    .profile-info-div{
        padding-top:80px;
        padding-bottom:0px;
        background-color: #212930 !important;
        border-top-right-radius:80px;
        border-top-left-radius:80px;
    }
    .profile-img-div{
        height:60px;
    }
    .profile-img-div img{
        margin-top:20px !important;
        z-index: 1;
    }
    @media(max-width:767px){
        .profile-info-div{
            padding-top:65px;
            border-top-right-radius:40px;
            border-top-left-radius:40px;
        }
    }
    
       .link-body{
      min-height:100vh;
   }
           .widget-input{
            /* background: rgba(0,0,0,0.4) !important; */
            background:rgba(255,255,255,0.5) !important;
        }
        
        .widget-input input::placeholder{
              color:rgba(0,9,0,0.5) !important;
        }
        .tiktok-video-thumbnail{
        width:100%;
        height:500px;
        background-repeat:no-repeat;
        background-position:center;
        background-size:cover;
        border:15px solid #212930;
        border-radius:35px;
        display:flex;
        align-items:center;
        justify-content:center;
        box-shadow: 0px 4px 30px rgba(6, 18, 81, 0.1);
    }
    .social-links-div svg{
        width: 26px !important;
    }
    .text-block-main{
        border-radius:40px;
    }
</style><link rel="stylesheet" href="https://app.znaplink.com/themes/altum/assets//growl-notification/colored-theme.min.css"></head>

    

<body class="link-body bg-white">
   <!-- <script src="https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.8.1/slick.min.js" integrity="sha512-XtmMtDEcNz2j7ekrtHvOVR4iwwaD6o/FUJe6+Zq+HgcCsk3kj4uSQQR8weQ2QVj1o0Pk6PwYLohm206ZzNfubg==" crossorigin="anonymous"></script> -->
   <link rel="stylesheet" href="https://app.znaplink.com/themes/altum/assets//slick/slick-theme.css">
   <link rel="stylesheet" href="https://app.znaplink.com/themes/altum/assets//slick/slick.css">
   <div class="profile-main  animate__animated animate__fadeIn">
       <div class="profile_banner_main"></div>
          <div class="">
         <div class="row m-0">
            <div class="col-lg-12 col-12 text-center profile-img-div">
               <img src="https://imagedelivery.net/tqC70bVt8T6GtQUXNsa2-g/6c636793-678b-4e46-dc8b-cc2ca58dde00/public" class="user-avatar">
            </div>
            <div class="col-lg-12 col-12 profile-info-div">
               <h2 class="profile_title d-flex align-items-center justify-content-center mt-2 mb-2">
               <span class="mr-2">MoiCbio </span>
                
                </h2>
               <!-- <small><strong>@MoiCbio</strong></small> -->
               <div class="profile_description pt-1 pb-1">
               <div>we're just still running  // welcome</div>
               </div>

                              <p class="profile_socials">
                                                      <span class="d-inline-flex align-items-center justify-content-center">
                     <a class="social-links-div " href="mailto: Mohammedeissaalshari@gmail.com" target="_blank">
                                                    <svg width="26" height="24" viewBox="0 0 85 68" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M0.872277 17.5707C-0.39581 29.2974 -0.339284 42.8221 1.42528 54.5012C2.40165 60.9635 7.70076 65.9177 14.242 66.4836L21.0781 67.0751C35.3325 68.3083 49.6675 68.3083 63.9218 67.075L70.758 66.4836C77.2992 65.9176 82.5983 60.9635 83.5747 54.5012C85.3392 42.8221 85.3959 29.2982 84.1278 17.5714C83.9638 16.2119 83.7794 14.8542 83.5747 13.4988C82.5983 7.03652 77.2992 2.08235 70.758 1.51641L63.9218 0.924952C49.6675 -0.308318 35.3325 -0.308317 21.0781 0.924953L14.242 1.51641C7.70076 2.08235 2.40165 7.03652 1.42528 13.4988C1.22053 14.854 1.03619 16.2114 0.872277 17.5707ZM21.6661 7.65744C35.5292 6.45802 49.4707 6.45802 63.3338 7.65744L70.17 8.2489C73.5845 8.54432 76.3506 11.1304 76.8603 14.5037C76.9132 14.8541 76.9647 15.2045 77.0148 15.5552L51.8426 29.4739C46.0323 32.6866 38.9673 32.6866 33.1571 29.4739L7.98512 15.5553C8.03519 15.2046 8.08669 14.8541 8.13963 14.5037C8.6493 11.1304 11.4154 8.54432 14.83 8.2489L21.6661 7.65744ZM77.8456 22.8265C78.7237 33.0433 78.3952 43.3371 76.8603 53.4963C76.3506 56.8696 73.5845 59.4557 70.17 59.7511L63.3338 60.3426C49.4707 61.542 35.5292 61.542 21.6661 60.3426L14.83 59.7511C11.4154 59.4557 8.6493 56.8696 8.13963 53.4963C6.60472 43.3372 6.27627 33.0434 7.15428 22.8267L29.8596 35.3813C37.7206 39.728 47.279 39.728 55.14 35.3813L77.8456 22.8265Z" fill="black"></path>
</svg>
                                             </a>
                  </span>
                                                                        <span class="d-inline-flex align-items-center justify-content-center">
                     <a class="social-links-div " href="tel: +31 6 28 89 03 03" target="_blank">
                                                    <svg width="26" height="22" viewBox="0 0 73 73" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M9.40261 28.3638C16.8518 44.594 30.1075 57.4974 46.5861 64.4892L46.6381 64.5113L49.8216 65.9311C53.8754 67.7382 58.6401 66.4547 61.2392 62.8555L66.5505 55.5002C66.875 55.0509 66.7913 54.4262 66.3602 54.0782L57.0879 46.5935C56.6269 46.2214 55.9491 46.308 55.5965 46.7841L51.9877 51.6566C51.1113 52.8399 49.5286 53.2511 48.1875 52.6439C35.8658 47.0643 25.9642 37.157 20.388 24.8281C19.7811 23.4863 20.192 21.9026 21.3746 21.0257L26.2442 17.4149C26.7201 17.062 26.8067 16.3838 26.4348 15.9226L18.9534 6.64365C18.6057 6.21239 17.9815 6.12862 17.5325 6.45295L10.1418 11.7915C6.52081 14.4071 5.24563 19.2147 7.0939 23.2826L9.40013 28.3584C9.40096 28.3602 9.40178 28.362 9.40261 28.3638ZM44.1192 70.237C26.2141 62.6323 11.8127 48.6076 3.71863 30.9685L3.71376 30.9579L1.40269 25.8714C-1.67775 19.0916 0.447539 11.0789 6.48247 6.71968L13.8732 1.3811C17.0163 -0.889208 21.3851 -0.302852 23.8191 2.71596L31.3005 11.9949C33.9036 15.2234 33.2973 19.9708 29.9665 22.4406L27.1762 24.5097C31.8896 33.6608 39.3599 41.1355 48.5058 45.8517L50.5737 43.0597C53.0421 39.727 57.7867 39.1203 61.0133 41.7249L70.2856 49.2096C73.3036 51.6458 73.8889 56.0188 71.6179 59.1637L66.3066 66.519C61.9748 72.5177 54.0335 74.6569 47.2773 71.645L44.1192 70.237Z" fill="black"></path>
</svg>
                                             </a>
                  </span>
                                                                        <span class="d-inline-flex align-items-center justify-content-center">
                     <a class="social-links-div " href="https://api.whatsapp.com/send?phone=+31 6 28 89 03 03" target="_blank">
                                                    <svg width="18" height="22" viewBox="0 0 83 83" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M28.3468 21.63C29.1093 21.6505 29.9547 21.6919 30.7589 23.4842C31.2923 24.6773 32.1907 26.8739 32.9226 28.6632C33.4921 30.0555 33.9607 31.2013 34.078 31.4358C34.346 31.9713 34.5109 32.5893 34.1605 33.3101C34.1191 33.3952 34.0801 33.4765 34.0425 33.5548C33.7614 34.1405 33.5613 34.5574 33.0886 35.1024C32.8942 35.3264 32.6917 35.5721 32.4899 35.8168C32.1351 36.2473 31.7826 36.675 31.4804 36.9771C30.9444 37.5123 30.3876 38.0896 31.006 39.1607C31.6248 40.2317 33.7895 43.7544 36.985 46.5972C40.4204 49.6677 43.4077 50.9617 44.9178 51.6158C45.211 51.7428 45.4485 51.8457 45.6227 51.9327C46.695 52.4683 47.3339 52.3858 47.9524 51.665C48.5712 50.9437 50.6325 48.5335 51.3542 47.4624C52.0552 46.3914 52.7766 46.5562 53.7663 46.9269C54.7558 47.2976 60.0334 49.8932 61.1053 50.4287C61.3172 50.5346 61.5154 50.63 61.6991 50.7185C62.445 51.0776 62.952 51.3216 63.167 51.6855C63.435 52.1386 63.435 54.2811 62.5486 56.7942C61.6416 59.3074 57.2709 61.7176 55.2917 61.903C55.1043 61.9207 54.9179 61.9434 54.7259 61.9667C52.9122 62.1869 50.6098 62.4666 42.4067 59.225C32.2989 55.2346 25.6266 45.3339 24.2776 43.3322C24.1711 43.1742 24.0978 43.0654 24.0586 43.0126L24.0357 42.982C23.422 42.1575 19.6673 37.1137 19.6673 31.9098C19.6673 26.9308 22.1104 24.3387 23.2247 23.1564C23.2953 23.0814 23.3606 23.0122 23.4196 22.9483C24.409 21.8772 25.5637 21.6095 26.2852 21.6095C27.007 21.6095 27.7284 21.6095 28.3468 21.63Z" fill="black"></path>
<path fill-rule="evenodd" clip-rule="evenodd" d="M0.41706 80.8802C0.0760863 82.1228 1.20335 83.2697 2.44548 82.9439L21.6467 77.909C27.7077 81.2049 34.5317 82.9559 41.4795 82.9559H41.5C64.363 82.9559 83 64.3541 83 41.4884C83 30.4057 78.6908 19.9819 70.857 12.1538C63.0231 4.32598 52.6118 0 41.4996 0C18.637 0 2.6435e-06 18.6017 2.6435e-06 41.4679C-0.00259546 48.7421 1.90996 55.889 5.54566 62.1912L0.41706 80.8802ZM11.5724 63.858C12.0176 62.2358 11.7952 60.502 10.9552 59.0459C7.87057 53.699 6.24908 47.6354 6.25129 41.4679C6.25129 22.0975 22.0598 6.27581 41.4996 6.27581C50.9595 6.27581 59.785 9.945 66.447 16.6018C73.1014 23.2513 76.7487 32.074 76.7487 41.4884C76.7487 60.8583 60.9403 76.6801 41.5 76.6801H41.4795C35.5761 76.6801 29.775 75.1917 24.624 72.3907C23.2299 71.6326 21.6009 71.4346 20.0669 71.8369L8.55447 74.8557L11.5724 63.858Z" fill="black"></path>
</svg>
                                             </a>
                  </span>
                                                                        <span class="d-inline-flex align-items-center justify-content-center">
                     <a class="social-links-div " href="https://facebook.com/profile.php?id=100009580001045" target="_blank">
                                                    <svg width="21" height="22" viewBox="0 0 83 81" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M41.5 6.225C22.1063 6.225 6.38461 21.5536 6.38461 40.4625C6.38461 57.7252 19.4881 72.0039 36.5263 74.3592V57.1077H30.3684C29.0604 57.1077 28 56.0401 28 54.7231V43.2769C28 41.9599 29.0604 40.8923 30.3684 40.8923H36.5263V34.6923C36.5263 30.2652 38.273 26.0195 41.3822 22.8891C44.4913 19.7586 48.7082 18 53.1052 18H61.6316C62.9396 18 64 19.0676 64 20.3846V31.8308C64 33.1478 62.9396 34.2154 61.6316 34.2154H53.1052C52.9796 34.2154 52.8591 34.2656 52.7703 34.3551C52.6815 34.4445 52.6316 34.5658 52.6316 34.6923V40.8923H61.6316C62.3609 40.8923 63.0495 41.2306 63.4984 41.8094C63.9472 42.3882 64.1061 43.1429 63.9293 43.8553L61.0872 55.3014C60.8236 56.363 59.8762 57.1077 58.7895 57.1077H52.6316V72.944C66.5691 68.4054 76.6154 55.5779 76.6154 40.4625C76.6154 21.5536 60.8937 6.225 41.5 6.225ZM51.1604 79.8229C69.4211 75.5781 83 59.5664 83 40.4625C83 18.1157 64.4198 0 41.5 0C18.5802 0 0 18.1157 0 40.4625C-1.95362e-06 62.8093 18.5802 80.925 41.5 80.925C44.5466 80.925 47.5166 80.6049 50.3764 79.9973C50.6528 79.9842 50.9167 79.9234 51.1604 79.8229ZM47.8947 74.1336V54.7231C47.8947 53.4061 48.9551 52.3385 50.2631 52.3385H56.9403L58.5981 45.6615H50.2631C48.9551 45.6615 47.8947 44.5939 47.8947 43.2769V34.6923C47.8947 33.3009 48.4437 31.9666 49.4209 30.9827C50.398 29.9989 51.7233 29.4462 53.1052 29.4462H59.2631V22.7692H53.1052C49.9645 22.7692 46.9524 24.0254 44.7316 26.2614C42.5108 28.4974 41.2631 31.5301 41.2631 34.6923V43.2769C41.2631 44.5939 40.2028 45.6615 38.8947 45.6615H32.7368V52.3385H38.8947C40.2028 52.3385 41.2631 53.4061 41.2631 54.7231V74.6992C41.342 74.6997 41.421 74.7 41.5 74.7C43.6839 74.7 45.8212 74.5056 47.8947 74.1336Z" fill="black"></path>
</svg>
                                             </a>
                  </span>
                                                                                                            <span class="d-inline-flex align-items-center justify-content-center">
                     <a class="social-links-div " href="https://instagram.com/moie._10" target="_blank">
                                                    <svg width="20" height="22" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M56.6428 19.2306C56.6428 16.9365 58.5056 15.0767 60.8035 15.0767C63.1014 15.0767 64.9642 16.9365 64.9642 19.2306C64.9642 21.5247 63.1014 23.3845 60.8035 23.3845C58.5056 23.3845 56.6428 21.5247 56.6428 19.2306Z" fill="#1A1923"></path>
<path fill-rule="evenodd" clip-rule="evenodd" d="M40 20.2691C29.085 20.2691 20.2367 29.1029 20.2367 40.0001C20.2367 50.8972 29.085 59.7311 40 59.7311C50.915 59.7311 59.7633 50.8972 59.7633 40.0001C59.7633 29.1029 50.915 20.2691 40 20.2691ZM26.4777 40.0001C26.4777 32.5441 32.5319 26.4999 40 26.4999C47.4682 26.4999 53.5223 32.5441 53.5223 40.0001C53.5223 47.456 47.4682 53.5002 40 53.5002C32.5319 53.5002 26.4777 47.456 26.4777 40.0001Z" fill="#1A1923"></path>
<path fill-rule="evenodd" clip-rule="evenodd" d="M61.878 1.9214C47.4547 0.312009 32.5455 0.312009 18.1221 1.9214C9.75053 2.85551 2.99216 9.43948 2.00793 17.8408C0.283163 32.5635 0.283163 47.4366 2.00793 62.1593C2.99216 70.5607 9.75053 77.1446 18.1221 78.0787C32.5455 79.6881 47.4547 79.6881 61.878 78.0787C70.2496 77.1446 77.008 70.5607 77.9922 62.1593C79.717 47.4366 79.717 32.5635 77.9922 17.8408C77.008 9.43948 70.2496 2.85551 61.878 1.9214ZM18.8153 8.11368C32.778 6.5557 47.2222 6.5557 61.1848 8.11368C66.719 8.73119 71.1522 13.0912 71.7934 18.5647C73.4618 32.8064 73.4618 47.1937 71.7934 61.4355C71.1522 66.909 66.719 71.2689 61.1848 71.8865C47.2222 73.4444 32.778 73.4444 18.8153 71.8865C13.2811 71.2689 8.84795 66.909 8.20673 61.4355C6.5383 47.1937 6.5383 32.8064 8.20673 18.5647C8.84795 13.0912 13.2811 8.73119 18.8153 8.11368Z" fill="#1A1923"></path>
</svg>
                                             </a>
                  </span>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       </p>
            </div>
         </div>
      </div>
   </div>
   <div class="container animate__animated animate__fadeIn">
      <div class="row d-flex justify-content-center text-center">
         <div class="col-md-12 link-content ">
                        <header class="d-none flex-column align-items-center" style="color: #fff">
               <img id="image" src="https://app.znaplink.com/uploads/avatars/https://imagedelivery.net/tqC70bVt8T6GtQUXNsa2-g/6c636793-678b-4e46-dc8b-cc2ca58dde00/public" alt="Avatar" class="link-image" style="display: none;">
               <div class="d-flex flex-row align-items-center mt-4">
                  <h1 id="title">MoiCbio</h1>
                                 </div>
               <p id="description">we're just still running  // welcome</p>
            </header>
            <main id="links" class="mt-4">
                                                                           <h3 class="pl-2 pt-3 d-none font-weight-medium2 folder-title">My Kit</h3>
               <div class="row links-slider-main mb-4 mt-2 d-none">
                  <div class="links-slider">
                                       </div>
               </div>
                                                                           <div class="row links-slider-main mb-4 mt-4 d-none">
                  <div class="links-slider" style="overflow:hidden;">
                                       </div>
               </div>
                                                                           <div class="row links-slider-main mb-1 mt-1 ">
                  <div class="links-slider pt-0 pb-0" style="overflow:hidden;">
                                                                                    
    <div class="single-link-block d-sm-block d-none d-xl-block d-lg-block d-md-block mt-0">
                                        <a href="https://pypi.org/project/moidata/">
                                            <div class="single-link-block-img">
                                            <div class="link-btn-image" style="background-image: url('https://imagedelivery.net/tqC70bVt8T6GtQUXNsa2-g/2402e787-4d6d-4cfd-dbb5-7fb6fb4a6b00/public?1653850234')"></div>
                                            </div>
                                            
                                            <div class="single-link-block-details">
                                                <h4>MoiData modules 😊</h4>
                                                <p>moidata library was created by Moieis</p>
                                            </div>
                                            
                                            <div class="single-link-block-arrow">
                                                
                                                <svg width="19" height="19" viewBox="0 0 24 23" fill="none" xmlns="http://www.w3.org/2000/svg">
                                                <rect x="20.3594" y="18.6191" width="18.619" height="2.73809" rx="1.36904" transform="rotate(-90 20.3594 18.6191)" fill="white"></rect>
                                                <rect x="4.47852" width="18.619" height="3.2857" rx="1.64285" fill="white"></rect>
                                                <rect x="22.4639" y="2.68164" width="28.7345" height="3.03407" rx="1.51704" transform="rotate(135 22.4639 2.68164)" fill="white"></rect>
                                                </svg>

                                            </div>

                                        </a>
    </div>

    
<div class="d-xl-none d-lg-none d-md-none d-sm-none d-block" style="flex:1">
<div data-link-id="215035" class="link-card link-card-single" style="width:100%;">
    <div>
    <a href="https://pypi.org/project/moidata/" data-link-url="amEGnJBfws" class="btn btn-block btn-primary link-btn " style="background: #fff;color: #000">
        <div class="link-btn-image-wrapper ">
            
        </div>

                <div class="link-img-div">
            <div class="link-btn-image lazy" style="background-image: url('https://imagedelivery.net/tqC70bVt8T6GtQUXNsa2-g/2402e787-4d6d-4cfd-dbb5-7fb6fb4a6b00/public?1653850234')"></div>
     
        </div>
        

        <h4 class="link-title">
        MoiData modules 😊        </h4>
        <p class="link-description text-muted pb-6">
        moidata library was created by Moieis        </p>
        
                <div class="div-block-342"><div class="text-block-20">DOOS 
        <!-- 🚀 -->
        </div></div>
        
        
    </a>
    </div>
    
</div>
        </div>

                                                            </div>
               </div>
                                                                           <div class="row links-slider-main mb-4 mt-4 d-none">
                  <div class="links-slider" style="overflow:hidden;">
                                       </div>
               </div>
                                                                           <div class="row links-slider-main mb-1 mt-1 ">
                  <div class="links-slider pt-0 pb-0" style="overflow:hidden;">
                                                                                    
    <div class="single-link-block d-sm-block d-none d-xl-block d-lg-block d-md-block mt-0">
                                        <a href="https://github.com/moieis">
                                            <div class="single-link-block-img">
                                            <div class="link-btn-image" style="background-image: url('https://imagedelivery.net/tqC70bVt8T6GtQUXNsa2-g/274a2f81-bb6e-493b-a025-bc7f9201e800/public?1653850234')"></div>
                                            </div>
                                            
                                            <div class="single-link-block-details">
                                                <h4>Moieis ✨</h4>
                                                <p>github account 👍🏻</p>
                                            </div>
                                            
                                            <div class="single-link-block-arrow">
                                                
                                                <svg width="19" height="19" viewBox="0 0 24 23" fill="none" xmlns="http://www.w3.org/2000/svg">
                                                <rect x="20.3594" y="18.6191" width="18.619" height="2.73809" rx="1.36904" transform="rotate(-90 20.3594 18.6191)" fill="white"></rect>
                                                <rect x="4.47852" width="18.619" height="3.2857" rx="1.64285" fill="white"></rect>
                                                <rect x="22.4639" y="2.68164" width="28.7345" height="3.03407" rx="1.51704" transform="rotate(135 22.4639 2.68164)" fill="white"></rect>
                                                </svg>

                                            </div>

                                        </a>
    </div>

    
<div class="d-xl-none d-lg-none d-md-none d-sm-none d-block" style="flex:1">
<div data-link-id="215063" class="link-card link-card-single" style="width:100%;">
    <div>
    <a href="https://github.com/moieis" data-link-url="3tdVSTilE8" class="btn btn-block btn-primary link-btn " style="background: #fff;color: #000">
        <div class="link-btn-image-wrapper ">
            
        </div>

                <div class="link-img-div">
            <div class="link-btn-image lazy" style="background-image: url('https://imagedelivery.net/tqC70bVt8T6GtQUXNsa2-g/274a2f81-bb6e-493b-a025-bc7f9201e800/public?1653850234')"></div>
     
        </div>
        

        <h4 class="link-title">
        Moieis ✨        </h4>
        <p class="link-description text-muted pb-6">
        github account 👍🏻        </p>
        
                <div class="div-block-342"><div class="text-block-20">DOOS 
        <!-- 🚀 -->
        </div></div>
        
        
    </a>
    </div>
    
</div>
        </div>

                                                            </div>
               </div>
                                                                           <div class="row links-slider-main mb-1 mt-1 ">
                  <div class="links-slider pt-0 pb-0" style="overflow:hidden;">
                                                                                    
    <div class="single-link-block d-sm-block d-none d-xl-block d-lg-block d-md-block mt-0">
                                        <a href="https://wowyamoi.nl">
                                            <div class="single-link-block-img">
                                            <div class="link-btn-image" style="background-image: url('https://imagedelivery.net/tqC70bVt8T6GtQUXNsa2-g/d287cd4f-de8b-45bf-1330-05b71ba1d400/public?1653850234')"></div>
                                            </div>
                                            
                                            <div class="single-link-block-details">
                                                <h4>e-commerce 🥳</h4>
                                                <p>Open soon ..</p>
                                            </div>
                                            
                                            <div class="single-link-block-arrow">
                                                
                                                <svg width="19" height="19" viewBox="0 0 24 23" fill="none" xmlns="http://www.w3.org/2000/svg">
                                                <rect x="20.3594" y="18.6191" width="18.619" height="2.73809" rx="1.36904" transform="rotate(-90 20.3594 18.6191)" fill="white"></rect>
                                                <rect x="4.47852" width="18.619" height="3.2857" rx="1.64285" fill="white"></rect>
                                                <rect x="22.4639" y="2.68164" width="28.7345" height="3.03407" rx="1.51704" transform="rotate(135 22.4639 2.68164)" fill="white"></rect>
                                                </svg>

                                            </div>

                                        </a>
    </div>

    
<div class="d-xl-none d-lg-none d-md-none d-sm-none d-block" style="flex:1">
<div data-link-id="215071" class="link-card link-card-single" style="width:100%;">
    <div>
    <a href="https://wowyamoi.nl" data-link-url="jOnUc3x6po" class="btn btn-block btn-primary link-btn " style="background: #fff;color: #000">
        <div class="link-btn-image-wrapper ">
            
        </div>

                <div class="link-img-div">
            <div class="link-btn-image lazy" style="background-image: url('https://imagedelivery.net/tqC70bVt8T6GtQUXNsa2-g/d287cd4f-de8b-45bf-1330-05b71ba1d400/public?1653850234')"></div>
     
        </div>
        

        <h4 class="link-title">
        e-commerce 🥳        </h4>
        <p class="link-description text-muted pb-6">
        Open soon ..        </p>
        
                <div class="div-block-342"><div class="text-block-20">DOOS 
        <!-- 🚀 -->
        </div></div>
        
        
    </a>
    </div>
    
</div>
        </div>

                                                            </div>
               </div>
                                                         </main>
                        
            
         </div>
      </div>
   </div>

<div class="modal fade" id="create_tiktok_widget" tabindex="-1" role="dialog" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content" style="height:100%;overflow:hidden">
            <div class="modal-header" style="padding:0;padding-bottom:10px;">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">×</span>
                </button>
            </div>
            <iframe scrolling="yes" src="" style="height:700px;width:auto;" id="tiktok_iframe" frameborder="0"></iframe>
            

        </div>
    </div>
</div>
   

    
<input type="hidden" id="url" name="url" value="https://app.znaplink.com/">
<input type="hidden" name="global_token" value="43ff0132edbb14d49dc211dd365f141e">
<input type="hidden" name="number_decimal_point" value=".">
<input type="hidden" name="number_thousands_separator" value=",">

<script>
    /* Some global variables */
    window.altum = {};
    let global_token = document.querySelector('input[name="global_token"]').value;
    let url = document.querySelector('input[name="url"]').value;
    let decimal_point = document.querySelector('[name="number_decimal_point"]').value;
    let thousands_separator = document.querySelector('[name="number_thousands_separator"]').value;
</script>

            <script src="https://app.znaplink.com/themes/altum/assets/js/libraries/jquery.min.js?v=2"></script>
            <script src="https://app.znaplink.com/themes/altum/assets/js/libraries/popper.min.js?v=2"></script>
            <script src="https://app.znaplink.com/themes/altum/assets/js/libraries/bootstrap.min.js?v=2"></script>
            <script src="https://app.znaplink.com/themes/altum/assets/js/main.js?v=2"></script>
            <script src="https://app.znaplink.com/themes/altum/assets/js/functions.js?v=2"></script>
            <script src="https://app.znaplink.com/themes/altum/assets/js/libraries/fontawesome.min.js?v=2"></script>
    
    <script src="https://app.znaplink.com/themes/altum/assets//slick/slick.min.js"></script>
<script src="https://app.znaplink.com/themes/altum/assets//growl-notification/growl-notification.min.js"></script>
<script>
$(".btn-tiktok-play").click(function(){
    $("#create_tiktok_widget").modal('show');
    $("#tiktok_iframe").attr('src',$(this).attr('data-url'));
});
$("#create_tiktok_widget").on('hidden.bs.modal',function(){
    $("#tiktok_iframe").attr('src','');
});
   if(window.innerWidth < 768) {
   //     $('.links-slider').slick({
   //   dots: false,
   //   infinite: false,
   //   speed: 300,
   //   slidesToShow: 4,
   //   arrows:false,
   //   responsive: [
   //     {
   //       breakpoint: 1024,
   //       settings: {
   //         slidesToShow: 3,
   //         slidesToScroll: 3,
   //         infinite: true,
   //         dots: false,
   //       }
   //     },
   //     {
   //       breakpoint: 767,
   //       settings: {
   //         slidesToShow: 2,
   //         slidesToScroll: 2,
   //       }
   //     },
   //     {
   //       breakpoint: 500,
   //       settings: {
   //         slidesToShow: 1,
   //         slidesToScroll: 1
   //       }
   //     }
   //     // You can unslick at a given breakpoint now by adding:
   //     // settings: "unslick"
   //     // instead of a settings object
   //   ]
   // });
   }
    
</script>
<script>
   /* Internal tracking for biolink links */
   $('[data-link-url]').on('click', event => {
   
       let base_url = $('[name="url"]').val();
       let url = $(event.currentTarget).data('link-url');
   
       $.ajax(`${base_url}${url}?no_redirect`);
   });
</script>
<script>
   /* Go over all mail buttons to make sure the user can still submit mail */
   $(".subscribe-btn").click(function(){
   var subscription_email = $(this).parent().find('input[name="email"]').val();
   var widget = $(this).parent().find('input[name="widget"]').val();
       $.ajax({
      url:"link-ajax",
      type: "POST",
      data:{
          token: 'a172928e8e307bc06c2a0da3b02d560f',
          request_type: 'subscribe',
          subscription_email:subscription_email,
          widget:widget
      },
      success:(data)=>
      {
          data = JSON.parse(data);
          if(data.status=='error'){
           GrowlNotification.notify({
                 description: data.message[0],
                 type: "error",
                 position: "top-right",
                 closeTimeout: 5000
             });
          }
          else{
           GrowlNotification.notify({
                 description: "Subscribed Successfully!",
                 type: "success",
                 position: "top-right",
                 closeTimeout: 5000
             });
             $(this).prev().prev().val('');
            $(this).prev().prev().attr('placeholder','Thanks! You\'re in.');
          }
          
      }
    });
   });
   $('form[id^="mail_"]').each((index, element) => {
       let link_id = $(element).find('input[name="link_id"]').val();
       let is_converted = localStorage.getItem(`mail_${link_id}`);
   
       if(is_converted) {
           /* Set the submit button to disabled */
           $(element).find('button[type="submit"]').attr('disabled', 'disabled');
       }
   });
       /* Form handling for mail submissions if any */
   $('form[id^="mail_"]').on('submit', event => {
       let base_url = $('[name="url"]').val();
       let link_id = $(event.currentTarget).find('input[name="link_id"]').val();
       let is_converted = localStorage.getItem(`mail_${link_id}`);
   
       if(!is_converted) {
   
           $.ajax({
               type: 'POST',
               url: `${base_url}link-ajax`,
               data: $(event.currentTarget).serialize(),
               success: (data) => {
                   let notification_container = $(event.currentTarget).find('.notification-container');
   
                   if (data.status == 'error') {
                       notification_container.html('');
   
                       display_notifications(data.message, 'error', notification_container);
                   } else if (data.status == 'success') {
   
                       display_notifications(data.message, 'success', notification_container);
   
                       setTimeout(() => {
   
                           /* Hide modal */
                           $(event.currentTarget).closest('.modal').modal('hide');
   
                           /* Remove the notification */
                           notification_container.html('');
   
                           /* Set the localstorage to mention that the user was converted */
                           localStorage.setItem(`mail_${link_id}`, true);
   
                           /* Set the submit button to disabled */
                           $(event.currentTarget).find('button[type="submit"]').attr('disabled', 'disabled');
   
                       }, 1000);
   
                   }
               },
               dataType: 'json'
           });
   
       }
   
       event.preventDefault();
   });
   
   
//    document.addEventListener("DOMContentLoaded", function() {
//    var lazyloadImages = document.querySelectorAll(".lazy");    
//    var lazyloadThrottleTimeout;
   
//    function lazyload () {
//    if(lazyloadThrottleTimeout) {
//      clearTimeout(lazyloadThrottleTimeout);
//    }    
   
//    lazyloadThrottleTimeout = setTimeout(function() {
//        var scrollTop = window.pageYOffset;
//        lazyloadImages.forEach(function(img) {
//            // console.log(img.offsetTop, window.innerHeight + scrollTop);
//            if(img.offsetTop < (window.innerHeight + scrollTop)) {
//              img.style.backgroundImage = `url('${img.dataset.src}')`;
//              img.classList.remove('lazy');
//            }
//        });
//        if(lazyloadImages.length == 0) { 
//          document.removeEventListener("scroll", lazyload);
//          window.removeEventListener("resize", lazyload);
//          window.removeEventListener("orientationChange", lazyload);
//        }
//    }, 20);
//    }
   
//    document.addEventListener("scroll", lazyload);
//    window.addEventListener("resize", lazyload);
//    window.addEventListener("orientationChange", lazyload);
   
//    setTimeout(()=>{
//    lazyload();
//    },100);
//    });
   
   // $(".link-img-div").css('height',parseInt($(".link-img-div").css('width').replace('px'))/1.77);
   // $(window).on("resize", function(event){
   //   $(".link-img-div").css('height',parseInt($(".link-img-div").css('width').replace('px'))/1.77);
   //   console.log( $(this).width()/1.77 );
   // });
</script>

</body></html>'''),None,None,None]])




app.add_url_rule('/tool', 'webio.view', webio_view(start)
                 , methods=['GET', 'POST', 'OPTIONS'])



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()
    start_server(start, port=32323,debug=True,max_payload_size='10000000',reconnect_timeout=4)