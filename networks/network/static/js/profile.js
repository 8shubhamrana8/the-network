document.addEventListener("DOMContentLoaded", () => {
    const followBtn = document.getElementById("follow-btn")
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

    if(followBtn) {
        followBtn.addEventListener("click", function () {
            const profileId = this.dataset.profileId;

            // Use fetch to send request
            fetch(`/followProfile/${profileId}`, {
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

                if(data.is_following) {
                    followBtn.textContent = "Unfollow"
                } else {
                    followBtn.textContent = "Follow"
                }

                document.getElementById("follower-count").textContent = data.follower_count

            })
            .catch(error => console.error("Error:", error));
        })
    }
})