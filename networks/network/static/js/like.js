document.addEventListener("DOMContentLoaded", () => {
    const likeBtns = document.querySelectorAll(".like-btn");
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

    likeBtns.forEach((btn) => {

        btn.addEventListener("click", (e) => {
            e.currentTarget.blur();
            const postId = e.currentTarget.dataset.postId;

            fetch(`/likePost/${postId}`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrfToken,
                    "Content-Type": "application/json"                    
                }
            }).then(response => response.json())
            .then(data => {
                if (data.error) {
                    console.log(data.error)
                    return
                }

                if (data.is_liked) {
                    btn.style.fill = "#ff4d6d";
                } else {
                    btn.style.fill = "none";
                }

                document.getElementById(`likes-count-${postId}`).textContent = data.liked_count

            })
        })
    })

})