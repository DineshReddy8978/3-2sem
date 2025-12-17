async function calculate() {
    const a = Number(document.getElementById("num1").value);
    const b = Number(document.getElementById("num2").value);

    const response = await fetch("http://127.0.0.1:5000/calculate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ operation: "add", a, b })
    });

    const data = await response.json();
    document.getElementById("display").value = data.result;
}
