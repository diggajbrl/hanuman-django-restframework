document.addEventListener("DOMContentLoaded", function () {
    const remindMeButton = document.getElementById("remindMeButton");
    const popup = document.querySelector(".popup");
    const overlay = document.querySelector(".overlay");

    remindMeButton.addEventListener("click", function () {
        popup.style.display = "block";
        overlay.style.display = "block";
    });

    overlay.addEventListener("click", function () {
        popup.style.display = "none";
        overlay.style.display = "none";
    });
});
