let changeColor = document.getElementById("changeColor");


changeColor.addEventListener("click", async () => {
    let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        chrome.tabs.sendMessage(tabs[0].id, { method: "getSelection" }, function (response) {
            sendServiceRequest(response.data);
        });
    });
});

function sendServiceRequest(selectedText) {
    var serviceCall = 'http://www.google.com/search?q=' + selectedText + "+definition+investopedia";
    chrome.tabs.create({ url: serviceCall });
}

