import React from "react"
import { useSelector, useDispatch } from "react-redux"

import "./DashBoard.css"
import DashBoardFilter from "./DashBoardFilter.jsx"
import CandidateContainer from "../../general/CandidateContainer.jsx"
import DashBoardHeaderFilter from "./DashBoardHeaderFilter.jsx"
import { setHeaderToggle } from "../../../store/slice/HeaderToggleSlice.js"


export default function DashBoard() {
    const header_toggle = useSelector(state => state.HeaderToggle.header_toggle)
    const candidates = useSelector(state => state.Manager.candidates)
    const filter = useSelector(state => state.Filter.filterToggle)

    const dispatch = useDispatch()
    const set_header_toggle = (obj) => dispatch(setHeaderToggle(obj))

    function handleScroll() {
        if (window.innerWidth / 1.7 < window.scrollY){
            set_header_toggle(false)
        } else {set_header_toggle(true)}
    }

    React.useEffect(() => {
        window.addEventListener('scroll', handleScroll)
        return () => {
            set_header_toggle(true)
            window.removeEventListener('scroll', handleScroll)
        }
    }, [])

    return(
        <>
        { filter ? <DashBoardFilter/> : 
        <>
        { !header_toggle ? <DashBoardHeaderFilter/> : "" }
        <div className="dashboard">
            { candidates[0] ? candidates.map((can) => <CandidateContainer candidate={can} key={can.id}/>) : ""}
        </div>
        </>
        }
        </>
    )
}