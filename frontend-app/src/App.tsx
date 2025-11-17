import { useMemo, useState } from 'react'

type LoanRequest = {
  applicant_name: string
  amount: number
  income: number
  credit_score: number
  existing_debt: number
}

type LoanResponse = {
  approved: boolean
  rate: number
  reason: string
}

const defaultRequest: LoanRequest = {
  applicant_name: 'Ada Lovelace',
  amount: 5000,
  income: 72000,
  credit_score: 720,
  existing_debt: 1000,
}

function formatRate(rate: number) {
  return `${(rate * 100).toFixed(2)}%`
}

function App() {
  const [form, setForm] = useState<LoanRequest>(defaultRequest)
  const [result, setResult] = useState<LoanResponse | null>(null)
  const [status, setStatus] = useState<'idle' | 'loading' | 'error'>('idle')

  const disabled = useMemo(() => status === 'loading', [status])

  async function submit() {
    setStatus('loading')
    try {
      const response = await fetch('/loans/eligibility', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form),
      })
      if (!response.ok) throw new Error('Request failed')
      const payload = (await response.json()) as LoanResponse
      setResult(payload)
      setStatus('idle')
    } catch (error) {
      console.error(error)
      setStatus('error')
    }
  }

  return (
    <main className="app">
      <header>
        <h1>LLM-assisted Loan Demo</h1>
        <p>Use the form to check sample eligibility through the FastAPI gateway.</p>
      </header>

      <section className="card">
        <div className="field">
          <label>Name</label>
          <input
            value={form.applicant_name}
            onChange={(e) => setForm({ ...form, applicant_name: e.target.value })}
            disabled={disabled}
          />
        </div>
        <div className="field">
          <label>Amount</label>
          <input
            type="number"
            value={form.amount}
            onChange={(e) => setForm({ ...form, amount: Number(e.target.value) })}
            disabled={disabled}
          />
        </div>
        <div className="field">
          <label>Income</label>
          <input
            type="number"
            value={form.income}
            onChange={(e) => setForm({ ...form, income: Number(e.target.value) })}
            disabled={disabled}
          />
        </div>
        <div className="field">
          <label>Credit score</label>
          <input
            type="number"
            value={form.credit_score}
            onChange={(e) => setForm({ ...form, credit_score: Number(e.target.value) })}
            disabled={disabled}
          />
        </div>
        <div className="field">
          <label>Existing debt</label>
          <input
            type="number"
            value={form.existing_debt}
            onChange={(e) => setForm({ ...form, existing_debt: Number(e.target.value) })}
            disabled={disabled}
          />
        </div>
        <button onClick={submit} disabled={disabled}>Check eligibility</button>
        {status === 'error' && <p className="error">Request failed. Check the API gateway.</p>}
      </section>

      {result && (
        <section className="card result">
          <h2>Decision</h2>
          <p className={result.approved ? 'approved' : 'declined'}>
            {result.approved ? 'Approved' : 'Declined'} · {formatRate(result.rate)}
          </p>
          <p className="muted">{result.reason}</p>
        </section>
      )}
    </main>
  )
}

export default App
