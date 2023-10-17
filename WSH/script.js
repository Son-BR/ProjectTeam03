const gensim = require('gensim');

function summarizeNews() {
    const newsUrl = document.getElementById('news-url').value;
    if (!newsUrl) {
        alert('뉴스 URL을 입력하세요.');
        return;
    }
    // 뉴스 내용을 가져오는 가상 함수
    function getNewsArticle(url) {
        const dummyNewsArticle = "뉴스 내용 (가상 내용)";
        return dummyNewsArticle;
    }

    // 뉴스 내용 요약
    const article = getNewsArticle(newsUrl);
    const summary = summarizeNewsArticle(article);

    // 결과 표시
    const summaryContainer = document.getElementById('summary-container');
    const summaryElement = document.getElementById('summary');
    summaryElement.textContent = summary;
    summaryContainer.classList.remove('hidden');
}

function summarizeNewsArticle(article) {
    const ratio = 0.2; // 요약 비율 (예: 20%)
    const summary = gensim.summarization.summarize(article, ratio);
    return summary;
}
