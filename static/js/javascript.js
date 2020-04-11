function readmorefun() {
  var dots = document.getElementById("dots");
  var moreText = document.getElementById("appfurtherdesc");
  var btnText = document.getElementById("readmore");

  if (dots.style.display === "none") {
    dots.style.display = "inline";
    btnText.innerHTML = "Read more";
    moreText.style.display = "none";
  } else {
    dots.style.display = "none";
    btnText.innerHTML = "Read less";
    moreText.style.display = "inline";
  }
}


$('.googlePlayButton').click(function(){
    var p;
    $(".googlePlayButton").attr("disabled", true);
    p = document.getElementById('package').value;

    $.ajax(
    {
        type:"GET",
        url: "googlePlay/",
        data:{
                 package: p
        },
        success: function( data )
        {
            $('#appCard').css("display","block");
            $("#errormessage").css("display","none");
            $('#appimage').attr('src', data['image']);
            $('#apptitle').html(data['title']);
            $('#appdesc').html(data['description']);
            $('#appfurtherdesc').html(data['furtherdescription']);
            $('#appview').html(data['numReview']);
            $('#appdownloads').html(" &nbsp Downloads <i class='glyphicon glyphicon-download-alt'> </i> &nbsp "+data['installs']);
            r=parseInt(data['rating'])
            var ans=''
            for (var i=0; i < r; i++) {
              ans = ans + '<i class="fas fa-star"></i>';
            }
            rd=parseFloat(data['rating']);
            rd=rd-Math.floor(rd);
            if (rd!=0){
              ans=ans+'<i class="fas fa-star-half-alt"></i>';
            }
            $('#apprating').html("&nbsp "+ans+" &nbsp"+ data['rating']);
            $('#appdev').html("Developer : " +data['developer']);
            $(".googlePlayButton").attr("disabled", false);

        },
        error: function(data) {
            $('#appCard').css("display","none");
            $("#errormessage").css("display","block");
            if($("#package").val == ''){
              $("#errormessage").html("Please enter package name.");
            } else {
            $("#errormessage").html("Please enter a valid package name.");
            }
            $(".googlePlayButton").attr("disabled", false);
        }
     });
});

$('.appStoreButton').click(function(){
    var id,name;
    $(".appStoreButton").attr("disabled", true);
    id = document.getElementById('appid').value;
    name = document.getElementById('appname').value;
    $.ajax(
    {
        type:"GET",
        url: "appStore/",
        data:{
                 appid: id,
                 appname: name
        },
        success: function( data )
        {
          $('#appCard').css("display","block");
          $("#errormessage").css("display","none");
          $('#appimage').attr('src', data['image']);
          $('#apptitle').html(data['title']);
          $('#appdesc').html(data['description']);
          $('#appfurtherdesc').html(data['furtherdescription']);
          $('#appview').html(data['numReview']);
          r=parseInt(data['rating'])
          var ans=''
          for (var i=0; i < r; i++) {
            ans = ans + '<i class="fas fa-star"></i>';
          }
          rd=parseFloat(data['rating']);
          rd=rd-Math.floor(rd);
          if (rd!=0){
            ans=ans+'<i class="fas fa-star-half-alt"></i>';
          }
          $('#apprating').html("&nbsp "+ans+" &nbsp"+ data['rating']);
          $('#appdev').html("Developer : " +data['developer']);
          $(".appStoreButton").attr("disabled", false);
        },
        error: function(data) {
            $('#appCard').css("display","none");
            $("#errormessage").css("display","block");
            if($("#appid").val == '' || $("#appname").val == ''){
              $("#errormessage").html("Please enter all the fields.");
            } else {
            $("#errormessage").html("Please enter a valid Application ID.");
            }
            $(".appStoreButton").attr("disabled", false);
        }
     });
});


$('#search-box input').on('change', function() {
 if($('input[name=storeRadio]:checked', '#search-box').val()=='appStore'){
   $('.further-form-appStore').css("display","block");
   $("#errormessage").css("display","none");
   $('.further-form-googlePlay').css("display","none");
   $('#appCard').css("display","none");
   $('#appname').val("");
   $('#appid').val("");

 } else {
   $('.further-form-appStore').css("display","none");
   $("#errormessage").css("display","none");
   $('.further-form-googlePlay').css("display","block");
   $('#appCard').css("display","none");
   $('#package').val("");
 }
});


$('.keywordFinderButton').click(function(){
    var url;
    $(".keywordFinderButton").attr("disabled", true);
    url = document.getElementById('websiteurl').value;

    $.ajax(
    {
        type:"GET",
        url: "urlkeyword/",
        data:{
                 url: url
        },
        success: function( data )
        {
          if( data['v']==1){
            $("#errormessage").css("display","block");
            $("#errormessage").html("Please enter a valid URL.");
          }
          if(data['v']==2){
            $("#errormessage").css("display","block");
            $("#errormessage").html("Please enter in the URL field.");
          }
          if (data['v']==0){
            $('#keywordCard').css("display","block");
            $("#errormessage").css("display","none");
            var a='<ul>';
            var i;
            for (i = 0; i < data['keywords'].length; i++) {
                a=a+"<li>"+data['keywords'][i]+"</li>";
            }
            a=a+"</ul>";
            $('#keywordContent1').html(a);
            if(data['reckeywords']!=''){
              $('#keywordTitle').html('Recommended Keywords');
              var a='<ul>';
              var i;
              for (i = 0; i < data['reckeywords'].length; i++) {
                  a=a+"<li>"+data['reckeywords'][i]+"</li>";
              }
              a=a+"</ul>";
              $('#keywordContent2').html(a);
            }
          }
          $(".keywordFinderButton").attr("disabled", false);

        },
        error: function(data) {
          $('#keywordCard').css("display","none");
          $("#errormessage").css("display","block");
          $("#errormessage").html("Please enter a validd URL.");
          $(".keywordFinderButton").attr("disabled", false);
        }
     });
});
