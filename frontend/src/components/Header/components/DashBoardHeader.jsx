import React from "react"
import { useSelector, useDispatch } from "react-redux"

import "./DashBoardHeader.css"
import Logo2SVG from "../../SVG/Logo2.jsx"
import ArrowRightSVG from "../../SVG/ArrowRight.jsx"
import FilterSVG from "../../SVG/Filter.jsx"
import { setFilterToggle } from "../../../store/slice/FilterSlice.js"


export default function DashBoardHeader() {
    const manager = useSelector(state => state.Manager.manager)

    const dispatch = useDispatch()
    const set_filter_toggle = (obj) => dispatch(setFilterToggle(obj))

    const order = React.useRef()

    function openFilter() {
        set_filter_toggle()
    }

    function orderClick() {
        order.current.classList.toggle("rotate-svg-90")
        order.current.classList.toggle("rotate-svg-270")
    }
    
    return(
        <div className="dashboarg-header">
            <div className="dashboarg-header-title">
                <Logo2SVG/>
                <h1>Витрина кандидатов</h1>
            </div>
            <div className="dashboarg-header-content">
                <div className="dashboarg-header-filter">
                    <input className="db-b-i bg-input" type="text" placeholder="ФИО кандидата" name="fio"/>
                    <div><button className="dashboarg-header-filter-open db-b-i bg-input" onClick={openFilter}><FilterSVG fill="white"/></button></div>
                    <div className="dashboarg-header-filter-order db-b-i bg-input color-white-70" onClick={orderClick}>
                        <p>сначала приглашенные</p>
                        <div className="dashboarg-header-arrowsvg rotate-svg-90" ref={order}><ArrowRightSVG fill="white"/></div>
                    </div>
                </div>
                <div className="dashboarg-header-infobox">
                    <div className="dashboarg-header-infobox-count">
                        {manager.quotas}
                    </div>
                    <div className="dashboarg-header-infobox-name">доступных квот</div>
                </div>
            </div>
        </div>
    )
}