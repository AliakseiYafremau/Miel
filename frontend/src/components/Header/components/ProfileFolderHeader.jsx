import React from "react"
import { useDispatch } from "react-redux"
import { useNavigate, useLocation } from "react-router"

import "./ProfileFolderHeader.css"
import ArrowRightSVG from "../../SVG/ArrowRight.jsx"
import { setChangePage } from "../../../store/slice/pageSlice.js"


export default function ProfileFolderHeader() {
    const dispatch = useDispatch()
    const set_change = (obj) => dispatch(setChangePage(obj))

    const navigate = useNavigate()

    const pathname = useLocation().pathname

    function pageTransitions() {
        set_change(true)
        setTimeout(() => {
            navigate("/profile")
            set_change(false)
        }, 500)
    }

    React.useEffect(() => {
    }, [])

    return(
            <div className="profile-folder-header">
                <div className="rotate-svg-180" onClick={pageTransitions}><ArrowRightSVG fill="white"/></div>
                {pathname == "/profile/team" ? <h1>Моя команда</h1> : ""}
                {pathname == "/profile/favorites" ? <h1>Избранные кандидаты</h1> : ""}
                {pathname == "/profile/note" ? <h1>Заметки</h1> : ""}
                {pathname == "/profile/history" ? <h1>История приглашений</h1> : ""}
            </div>
    )
}