document.addEventListener("DOMContentLoaded", function () {

    let startTime = null;

    const textarea = document.getElementById("inputText");
    const form = document.querySelector("form");

    // ⌨️ Start timer on first key press
    textarea.addEventListener("input", function () {
        if (startTime === null) {
            startTime = Date.now();
        }
    });

    // 📤 On submit → calculate time + WPM
    form.addEventListener("submit", function () {

        if (startTime === null) return;

        const endTime = Date.now();
        const timeTaken = (endTime - startTime) / 1000;

        const text = textarea.value.trim();
        const wordCount = text.split(/\s+/).length;

        const wpm = (wordCount / timeTaken) * 60;

        // set hidden values
        document.getElementById("time_taken").value = timeTaken.toFixed(2);
        document.getElementById("wpm").value = wpm.toFixed(2);
    });

});