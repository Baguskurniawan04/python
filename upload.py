<!DOCTYPE html>
<html>
<head>
<title>Upload</title>
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
 <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
 <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
</head>
<body>

<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href="http://bagus01.pythonanywhere.com/gallery">Gallery</span></a>
      </li>
    </ul>
</nav>

<div class="container text-center mt-5">

    <form id="upload-form" action="{{ url_for('upload') }}" method="POST" enctype="multipart/form-data">

        <div class="custom-file">
          <input type="file" class="custom-file-input" name="file" id="file-picker" accept="image/*" multiple>
          <label class="custom-file-label" for="customFile">Choose file</label>
        </div>

        <div id="msg" class="lg-center mt-2"></div>

        <div class="mt-3">
            <input type="submit" value="UPLOAD GAN" id="upload-button" style="display:none;padding:7px 10px;border-radius:4px;background:#4C9AE8;border: none;color:#fff;">
        </div>
    </form>

</div>

<div class="mt-5">
    <h3 class="mb-4 text-center"> Nama </h3>
    <ul class="list-group" style="margin:0 auto;width:400px">
        <li class="list-group-item"> Bagus Kurniawan Adhi H (17.01.53.0018)</li>
    </ul>
</div>

</body>
<script>

    $("#file-picker").change(function(){

        var input = document.getElementById('file-picker');

        for (var i=0; i<input.files.length; i++)
        {
        //koala.jpg, koala.JPG substring(index) lastIndexOf('a') koala.1.jpg
            var ext= input.files[i].name.substring(input.files[i].name.lastIndexOf('.')+1).toLowerCase()

            if ((ext == 'jpg') || (ext == 'png'))
            {
                $("#upload-button").show();
                $("#msg").text("File support untuk di upload :)");
            }
            else
            {
                $("#upload-button").hide();
                $("#msg").text("File tidak support :(")
                document.getElementById("file-picker").value ="";
            }

        }


    } );

</script>
</html>