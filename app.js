import { useState } from "react";

function App() {
  const [value, setValue] = useState("");

  const handleClick = (v) => setValue(value + v);
  const clear = () => setValue("");

  const calculate = async () => {
    const res = await fetch("http://127.0.0.1:5000/calculate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ operation: "eval", a: value })
    });
    const data = await res.json();
    setValue(data.result);
  };

  return (
    <div>
      <input value={value} readOnly />
      <button onClick={() => handleClick("1")}>1</button>
      <button onClick={() => handleClick("+")}>+</button>
      <button onClick={calculate}>=</button>
      <button onClick={clear}>C</button>
    </div>
  );
}

export default App;
