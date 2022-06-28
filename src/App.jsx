import axios from "axios";
import { useEffect, useState } from "react";
import { ArrowFatLinesRight } from "phosphor-react";
import "./styles/app.css";

function App() {
	const [amount, setAmount] = useState(1);
	const [result, setResult] = useState(1);
	const [fromCurrency, setFromCurrency] = useState("AUD");
	const [toCurrency, setToCurrency] = useState("AUD");
	const [rates, setRates] = useState([]);

	useEffect(() => {
		axios
			.get("https://api.frankfurter.app/latest")
			.then(response => setRates(response.data.rates));
	}, []);

	async function handleChangeAmount(value) {
		setAmount(value);

		if (fromCurrency === toCurrency) {
			setResult(value);
			return;
		}

		await convert(fromCurrency, toCurrency);
	}

	function handleChangeFromCurrency(value) {
		setFromCurrency(value);
		convert(value, toCurrency);
	}

	function handleChangeToCurrency(value) {
		setToCurrency(value);
		convert(fromCurrency, value);
	}

	async function convert(fromCurrency, toCurrency) {
		if (!amount) return;

		const number = await axios
			.get(
				`https://api.frankfurter.app/latest?amount=${amount}&from=${fromCurrency}&to=${toCurrency}`
			)
			.then(response => response.data)
			.then(data => Object.values(data.rates)[0])
			.catch(error => console.error(error));

		return setResult(number);
	}

	return (
		<div className="container">
			<h1>Currency Converter</h1>

			<label htmlFor="amount">Enter Amount :</label>
			<input
				type="number"
				placeholder="Enter amount"
				value={amount}
				onChange={event => handleChangeAmount(event.target.value)}
			/>

			<div className="from-to">
				<div className="from-group">
					<label htmlFor="from-currency">From :</label>
					<select
						id="from-currency"
						onChange={event =>
							handleChangeFromCurrency(event.target.value)
						}
					>
						{Object.keys(rates).map(rate => (
							<option key={rate} value={rate}>
								{rate}
							</option>
						))}
					</select>
				</div>

				<ArrowFatLinesRight size={32} color="white" className="arrow" />

				<div className="to-group">
					<label htmlFor="to-currency">To :</label>
					<select
						id="to-currency"
						onChange={event =>
							handleChangeToCurrency(event.target.value)
						}
					>
						{Object.keys(rates).map(rate => (
							<option key={rate} value={rate}>
								{rate}
							</option>
						))}
					</select>
				</div>
			</div>

			{amount ? (
				<span>
					{amount} {fromCurrency} = {result} {toCurrency}
				</span>
			) : (
				""
			)}
		</div>
	);
}

export default App;
