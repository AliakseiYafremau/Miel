import React from "react"
import { useSelector, useDispatch } from "react-redux"
import { useNavigate } from "react-router"

import "./Intro.css"
import { setChangePage } from "../../../store/slice/pageSlice"
import { setCandidates, setManager } from "../../../store/slice/ManagerSlice"
import { get } from "../../../export/api/api"


export default function Intro() {
    const dispatch = useDispatch()
    const set_change = (obj) => dispatch(setChangePage(obj))
    const set_manager = (obj) => dispatch(setManager(obj))
    const set_candidates = (obj) => dispatch(setCandidates(obj))

    const startPage = useSelector(state => state.Page.startPage)

    const navigate = useNavigate()

    async function getManager() {
        await get("manager/")
        .then(json => {
            if (!json.error && !json.detail) {
                set_manager(json)
                getCandidates()
            } else {
                localStorage.removeItem("token")
                pageTransitions("login")
            }
        })
    }

    async function getCandidates() {
        await get("manager/get_available_candidates")
        .then(json => {
            set_candidates(json)
            if (startPage == "" || startPage == "/" || startPage == "/login") {
                pageTransitions("home")
            } else {
                pageTransitions(startPage)
            }
        })
    }

    React.useEffect(() => {
        if (localStorage.getItem("token")) {
            getManager()
        }
    },[])

    function pageTransitions(page) {
        setTimeout(() => {
            set_change(true)
            setTimeout(() => {
                navigate(page)
                set_change(false)
            }, 500)
        }, 2500)
    }
    
    return(
        <div className="intro"/>
    )
}