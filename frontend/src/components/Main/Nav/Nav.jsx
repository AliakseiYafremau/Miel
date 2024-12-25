import React, { useEffect } from "react"
import { useDispatch } from "react-redux"
import { useNavigate, useLocation } from "react-router"

import "./Nav.css"
import { setChangePage } from "../../../store/slice/pageSlice"
import { setCandidates, setManager } from "../../../store/slice/ManagerSlice"
import { get } from "../../../export/api/api"


export default function Nav() {
    const ball = React.useRef()
    const leftico = React.useRef()
    const rightico = React.useRef()
    const maskButton = React.useRef()

    const dispatch = useDispatch()
    const set_change = (obj) => dispatch(setChangePage(obj))

    const set_manager = (obj) => dispatch(setManager(obj))
    const set_candidates = (obj) => dispatch(setCandidates(obj))

    const navigate = useNavigate()
    const pathname = useLocation().pathname

    async function getCandidates() {
        await get("manager/get_available_candidates")
        .then(json => {
            set_candidates(json)
        })
    }

    async function getManager() {
        await get("manager/")
        .then(json => {
            if (!json.error && !json.detail) {
                set_manager(json)
            }
        })
    }

    function buttonHome() {
        getCandidates()
        navToggle("left")
        pageTransitions("home")
    }

    function buttonPerson() {
        getManager()
        navToggle("right")
        pageTransitions("profile")
    }

    function navToggle(direction) {
        if (direction == "left") {
            ball.current.classList.remove("left")
    
            leftico.current.classList.remove("down")
            leftico.current.classList.add("up")
            
            rightico.current.classList.remove("up")
            rightico.current.classList.add("down")    
    
            maskButton.current.classList.remove("right")
        } else {
            ball.current.classList.add("left")
    
            leftico.current.classList.remove("up")
            leftico.current.classList.add("down")
            
            rightico.current.classList.remove("down")
            rightico.current.classList.add("up")
    
            maskButton.current.classList.add("right")
        }
    }

    function pageTransitions(page) {
        set_change(true)
        setTimeout(() => {
            navigate(page)
            set_change(false)
        }, 500)
    }
    useEffect(() => {
        if (pathname.startsWith("/profile")) {
            navToggle("right")
        } else {
            navToggle("left")
        }
    }, [pathname])

    return(
        <>
        <div className="nav-container">
            <div className="nav-button-ico-container">
                <div className="nav-button-ico-co">
                    <svg className="nav-button-ico nav-button-ico-left" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" ref={leftico}>
                        <path d="M6 19H9V13H15V19H18V10L12 5.5L6 10V19ZM4 21V9L12 3L20 9V21H13V15H11V21H4Z"/>
                    </svg>
                </div>
                <div className="nav-button-ico-co">
                    <svg className="nav-button-ico nav-button-ico-right" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" ref={rightico}>
                        <path d="M12 12C10.9 12 9.95833 11.6083 9.175 10.825C8.39167 10.0417 8 9.1 8 8C8 6.9 8.39167 5.95833 9.175 5.175C9.95833 4.39167 10.9 4 12 4C13.1 4 14.0417 4.39167 14.825 5.175C15.6083 5.95833 16 6.9 16 8C16 9.1 15.6083 10.0417 14.825 10.825C14.0417 11.6083 13.1 12 12 12ZM4 20V17.2C4 16.6333 4.14583 16.1125 4.4375 15.6375C4.72917 15.1625 5.11667 14.8 5.6 14.55C6.63333 14.0333 7.68333 13.6458 8.75 13.3875C9.81667 13.1292 10.9 13 12 13C13.1 13 14.1833 13.1292 15.25 13.3875C16.3167 13.6458 17.3667 14.0333 18.4 14.55C18.8833 14.8 19.2708 15.1625 19.5625 15.6375C19.8542 16.1125 20 16.6333 20 17.2V20H4ZM6 18H18V17.2C18 17.0167 17.9542 16.85 17.8625 16.7C17.7708 16.55 17.65 16.4333 17.5 16.35C16.6 15.9 15.6917 15.5625 14.775 15.3375C13.8583 15.1125 12.9333 15 12 15C11.0667 15 10.1417 15.1125 9.225 15.3375C8.30833 15.5625 7.4 15.9 6.5 16.35C6.35 16.4333 6.22917 16.55 6.1375 16.7C6.04583 16.85 6 17.0167 6 17.2V18ZM12 10C12.55 10 13.0208 9.80417 13.4125 9.4125C13.8042 9.02083 14 8.55 14 8C14 7.45 13.8042 6.97917 13.4125 6.5875C13.0208 6.19583 12.55 6 12 6C11.45 6 10.9792 6.19583 10.5875 6.5875C10.1958 6.97917 10 7.45 10 8C10 8.55 10.1958 9.02083 10.5875 9.4125C10.9792 9.80417 11.45 10 12 10Z"/>
                    </svg>
                </div>
            </div>
            <div className="nav-ball-container" ref={ball}>
                <svg className="nav-ball-svg" viewBox="0 0 69 52" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <circle className="fill-secondary-5" cx="35" cy="22" r="22"/>
                </svg>
            </div>
            <div className="nav-content">
                <div className="nav-button" ref={maskButton}/>
            </div>
            <div className="nav-hidden">
                <div className="nav-hidden-button" onClick={buttonHome} unselectable="on"/>
                <div className="nav-hidden-button" onClick={buttonPerson}/>
            </div>
        </div>
        </>
    )
}