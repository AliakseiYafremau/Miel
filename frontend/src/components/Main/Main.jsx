import React from "react"
import { Route, Routes, useNavigate } from "react-router-dom"
import { useSelector, useDispatch } from "react-redux"
import { useLocation } from "react-router"

import "./Main.css"
import Intro from "./Intro/Intro.jsx"
import Nav from "./Nav/Nav.jsx"
import LoginForm from "./LoginForm/LoginForm.jsx"
import Profile from "./Profile/Profile.jsx"
import DashBoard from "./DashBoard/DashBoard.jsx"
import Candidate from "./Candidate/Candidate.jsx"
import ProfileFolder from "./ProfileFolder/ProfileFolder.jsx"
import { setStartPage } from "../../store/slice/pageSlice.js"

export default function Main() {
    const dispatch = useDispatch()
    const set_start_page = (obj) => dispatch(setStartPage(obj))

    const change = useSelector(state => state.Page.change.payload)
    const manager = useSelector(state => state.Manager.manager)
    const filter = useSelector(state => state.Filter.filterToggle)
    const mainEl = React.useRef()

    const navigate = useNavigate()
    const pathname = useLocation()

    React.useEffect(() => {        
        set_start_page(pathname.pathname + pathname.search)        
        if (!localStorage.token) {
            navigate("login")
        } else if (!!manager) {navigate("")}
    }, [])

    React.useEffect(() => {
        if (change) {
            mainEl.current.classList.add("m100")
            document.getElementById("root").classList.add("mh100")
            window.scrollTo(0, 0)
        } else {
            mainEl.current.classList.remove("m100")
            document.getElementById("root").classList.remove("mh100")
        }
    }, [change])

    return(
        <main ref={mainEl}>
            <div className="main">
                <Routes>
                    <Route path="" element={<Intro/>} />
                    <Route path="login" element={<LoginForm/>} />
                    <Route path="home" element={<DashBoard/>} />
                    <Route path="profile" element={<Profile/>} />
                    <Route path="profile/*" element={<ProfileFolder/>} />
                    <Route path="candidate" element={<Candidate/>} />
                </Routes>
                { pathname.pathname == "/" || pathname.pathname == "/login" || filter ? "" : <Nav/>}
            </div>
        </main>
    )
}