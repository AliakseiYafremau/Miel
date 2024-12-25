import React from "react"
import { useDispatch } from "react-redux"
import { useNavigate } from "react-router"

import "./LoginForm.css"
import { setChangePage } from "../../../store/slice/pageSlice"
import { post } from "../../../export/api/api"
import LoadingSVG from "../../SVG/Loading.jsx"


export default function LoginForm() {
    const dispatch = useDispatch()
    const set_change = (obj) => dispatch(setChangePage(obj))

    const navigate = useNavigate()

    const [email, setEmail] = React.useState("")
    const [password, setPassword] = React.useState("")
    const [error, setError] = React.useState(false)
    const [load, setLoad] = React.useState(false)

    const email_input_ref = React.useRef()
    const password_input_ref = React.useRef()

    function inputChange(e) {
        setError(false)
        e.target.value = e.target.value.replace(/\s/g, "")
        e.target.name == "email" ? setEmail(e.target.value) : setPassword(e.target.value)
    }

    async function login(){
        setLoad(true)
        const data = {
            email: email,
            password: password
        }        
        const token = await post("auth/login/", data)
        if (token.access_token) {
            localStorage.setItem("token", token.access_token)
            pageTransitions("/")
            setLoad(false)
        } else {
            setError(true)
            setPassword("")
            password_input_ref.current.value = ""
            setLoad(false)
        }
    }

    function pageTransitions(page) {
        set_change(true)
        setTimeout(() => {
            navigate(page)
            set_change(false)
        }, 500)
    }

    React.useEffect(() => {
    }, [])

    return(
        <div className="login-container-main bg-white">
            <div className="login-container-main-content">
                <form action="" autoComplete="on">
                    <div className="login-container">
                        <label htmlFor="email">e-mail:</label>
                        <input 
                        id="email"
                        name="email"
                        className={ error ? "login-input-username error" : "login-input-username"}
                        type="email"
                        autoComplete="on"
                        placeholder="Введите e-mail" 
                        onChange={inputChange} 
                        ref={email_input_ref}
                        />
                    </div>
                    <div className="login-container">
                        <label htmlFor="current-password">Пароль:</label>
                        <input 
                        id="current-password"
                        name="current-password"
                        type="password"
                        autoComplete="on"
                        className={ error ? "login-input-password error" : "login-input-password"}
                        placeholder="Введите пароль"
                        onChange={inputChange}
                        onKeyDown={(e) => e.key === "Enter" ? login() : ""}
                        ref={password_input_ref}/>
                        <a>Забыли пароль?</a>
                    </div>
                </form>
                <button onClick={load ? () => {} : login} type="button">
                    { load ? <div className="login-loading"><LoadingSVG fill="white"/></div> : "Вход"}
                </button>
            </div>
        </div>
    )
}