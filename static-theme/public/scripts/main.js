const $ = document;

const deleteBtns = $.querySelectorAll("#delete");

deleteBtns.forEach((btn) => {
    btn.addEventListener("click" , () => {
        window.location.href = "../../pages/confirm.html"
    })
})