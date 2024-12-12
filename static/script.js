document.getElementById("latency-form").addEventListener("submit", function (e) {
   e.preventDefault();

   const target = document.getElementById("target").value.trim();
   if (!target) {
       alert("Please enter a target address.");
       return;
   }

   const resultElement = document.getElementById("result");
   resultElement.textContent = "Testing latency...";

   fetch("/test_latency", {
       method: "POST",
       headers: { "Content-Type": "application/json" },
       body: JSON.stringify({ target: target }),
   })
       .then(response => response.json())
       .then(data => {
           if (data.output) {
               resultElement.textContent = data.output;
           } else if (data.error) {
               resultElement.textContent = `Error: ${data.error}`;
           }
       })
       .catch(error => {
           console.error("Error:", error);
           resultElement.textContent = "An error occurred. Please try again.";
       });
});
