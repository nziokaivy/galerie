showModal = (name,desc,url,loc,cat) => {
    console.log(name,desc,url)
    $("#label").text(name)
    $("#myModal").modal("show")
    $(".img-responsive").attr("src",url)
    $("#description").text(desc)
    $("#category").text("Category: " + cat)
    $("#location").text("Location: " + loc)   
    $("#url-copy").val(window.location.origin + url)
   
}
copyUrl = () => {
    $("#url-to-copy").select()
    document.execCommand('copy');
    alert("Link copied")
}