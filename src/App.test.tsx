import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import App from './App'

describe('App', () => {
  it('adds and toggles todos', async () => {
    render(<App />)
    const input = screen.getByPlaceholderText(/add new todo/i)
    await userEvent.type(input, 'first task')
    await userEvent.click(screen.getByRole('button', { name: /add/i }))

    const item = screen.getByText('first task')
    expect(item).toBeInTheDocument()
    const checkbox = screen.getByRole('checkbox')
    expect(checkbox).not.toBeChecked()

    await userEvent.click(checkbox)
    expect(checkbox).toBeChecked()
  })
})

