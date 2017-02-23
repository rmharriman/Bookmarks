var bookmarks = new can.Observe.List([
        {url:"http://one.com", title: "One"},
        {url:"http://two.com", title: "Two"}
    ]);

$(document).ready(function () {

    var viewModel = {bookmarks:bookmarks};
    var element = $("#container");
    element.html(can.view("/static/bookmark_list", viewModel));

});
