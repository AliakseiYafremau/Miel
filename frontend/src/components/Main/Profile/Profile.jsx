import React from "react"
import { useDispatch } from "react-redux"
import { useNavigate } from "react-router"

import "./Profile.css"
import ArrowRight from "../../SVG/ArrowRight.jsx"
import CycleSVG from "../../SVG/Cycle.jsx"
import StickyNoteSVG from "../../SVG/StickyNote.jsx"
import StarSVG from "../../SVG/Star.jsx"
import GroupsSVG from "../../SVG/Groups.jsx"
import { setChangePage } from "../../../store/slice/pageSlice.js"


export default function Profile() {
    const dispatch = useDispatch()
    const set_change = (obj) => dispatch(setChangePage(obj))

    const navigate = useNavigate()

    function switchPage(e) {
        const id = e.currentTarget.id
        switch (id) {
            case "profile-team":
                pageTransitions("team")
                break
            case "profile-favorites":
                pageTransitions("favorites")
                break
            case "profile-note":
                pageTransitions("note")
                break
            case "profile-history":
                pageTransitions("history")
                break
        }
        pageTransitions(5)
    }

    function pageTransitions(page) {
        set_change(true)
        setTimeout(() => {
            navigate(page)
            set_change(false)
        }, 500)
    }
    
    return(
            <div className="profile">
                <div id="profile-team" onClick={switchPage}><div ><GroupsSVG/>Моя команда</div><ArrowRight fill="black"/></div>
                <div id="profile-favorites" onClick={switchPage}><div><StarSVG fill="black"/>Избранные кандидаты</div><ArrowRight fill="black"/></div>
                <div id="profile-note" onClick={switchPage}><div><StickyNoteSVG fill="black"/>Заметки</div><ArrowRight fill="black"/></div>
                <div id="profile-history" onClick={switchPage}><div><CycleSVG/>История приглашений</div><ArrowRight fill="black"/></div>
            </div>
    )
}