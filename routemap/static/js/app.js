document.addEventListener("DOMContentLoaded", function () {
    let rows = document.querySelectorAll("#details");
    rows.forEach(function (row) {
        row.addEventListener("click", function () {
            this.parentElement.parentElement.nextElementSibling.classList.toggle("hidden");
            // this.parentElement.nextElementSibling.classList.toggle("hidden");
        });
    });
});

document.addEventListener("DOMContentLoaded", function () {
    let btn = document.querySelector("#add_list");
    btn.addEventListener("click", function () {
        this.nextElementSibling.classList.toggle("none_display");
    });
});

document.addEventListener("DOMContentLoaded", function () {
    let lists = document.querySelectorAll("#list_name");
    lists.forEach(function (list) {
        list.addEventListener("click", function () {
            this.nextElementSibling.classList.toggle("hidden")
        });
    });
});


document.addEventListener("DOMContentLoaded", function () {
    let side_menu = document.querySelectorAll('#side_menu');
    side_menu.forEach(function (link) {
        link.addEventListener("mouseover", function () {
            this.style.backgroundColor = "#413e3e";
        })
        link.addEventListener("mouseout", function () {
            this.style.backgroundColor = "#7f7e84";
        })
    })
})

document.addEventListener("DOMContentLoaded", function () {
    let header_links = document.querySelectorAll('.header_links');
    header_links.forEach(function (link) {
        link.addEventListener("mouseover", function () {
            this.style.backgroundColor = "#4b4d4b";
            this.style.color = "whitesmoke";
            // this.style.borderColor = "whitesmoke"
        })
        link.addEventListener("mouseout", function () {
            this.style.backgroundColor = "#84a6cc";
            this.style.color = "#4b4d4b";
            // this.style.borderColor = "#2d4373"
        })
    })
})


$(window).on("load resize ", function() {
  var scrollWidth = $('.tbl-content').width() - $('.tbl-content table').width();
  $('.tbl-header').css({'padding-right':scrollWidth});
}).resize();

// document.addEventListener("DOMContentLoaded", function () {
//     let nav = document.querySelector("#nav");
//     btn.addEventListener("click", function () {
//         this.classList.toggle("none-display");
//     });
// });