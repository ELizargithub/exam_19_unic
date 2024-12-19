document.addEventListener("DOMContentLoaded", function () {
    const originalText = "{{ text_data.original_text|escapejs }}";
    const cleanedText = "{{ text_data.cleaned_text|escapejs }}";

    const originalWords = originalText.split(" ");
    const cleanedWords = cleanedText.split(" ");

    let highlightedText = "";

    for (let i = 0; i < cleanedWords.length; i++) {
        if (originalWords[i] !== cleanedWords[i]) {
            highlightedText += `<span class='highlight'>${cleanedWords[i]}</span> `;
        } else {
            highlightedText += `${cleanedWords[i]} `;
        }
    }

    document.querySelector(".cleaned-text").innerHTML = highlightedText.trim();
});
