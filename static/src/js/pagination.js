document.addEventListener('DOMContentLoaded', function() {
    const reviewList = document.querySelector('.review-list');
    const prevPageBtn = document.querySelector('.prev-page');
    const nextPageBtn = document.querySelector('.next-page');
    const currentPageSpan = document.querySelector('.current-page');
    let cards = document.querySelectorAll(".review-card");

    // Предположим, что у вас есть массив отзывов
    const reviews = Array.from(reviewList.querySelectorAll('.review-card')).map(reviewCard => {
        const avatarUrl = reviewCard.querySelector('img').src;
        const username = reviewCard.querySelector('h3').textContent;
        const text = reviewCard.querySelector('p').textContent;
    
        return { avatarUrl, username, text };
    });

    console.log(reviews);
    

    const reviewsPerPage = 5; // Количество отзывов на одной странице
    let currentPage = 1;

    function displayReviews(pageNum) {
    const startIndex = (pageNum - 1) * reviewsPerPage;
    const endIndex = startIndex + reviewsPerPage;
    const pageReviews = reviews.slice(startIndex, endIndex);

    reviewList.innerHTML = '';
    pageReviews.forEach(review => {
        const reviewCard = document.createElement('div');
        reviewCard.classList.add('review-card');
        reviewCard.innerHTML = `
        <img src="${review.avatarUrl}" alt="Аватар пользователя">
        <div class="review-content">
            <h3>${review.username}</h3>
            <p>${review.text}</p>
        </div>
        `;
        reviewList.appendChild(reviewCard);
    });

    currentPageSpan.textContent = pageNum;
    prevPageBtn.disabled = pageNum === 1;
    nextPageBtn.disabled = endIndex >= reviews.length;
    }

    prevPageBtn.addEventListener('click', () => {
    currentPage--;
    displayReviews(currentPage);
    });

    nextPageBtn.addEventListener('click', () => {
    currentPage++;
    displayReviews(currentPage);
    });

    displayReviews(1); // Отображаем первую страницу отзывов при загрузке
})