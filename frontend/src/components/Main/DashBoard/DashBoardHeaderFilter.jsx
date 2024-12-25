import React from "react"
import { useSelector } from "react-redux"

import "./DashBoardHeaderFilter.css"
import ArrowRightSVG from "../../SVG/ArrowRight.jsx"
import FilterSVG from "../../SVG/Filter.jsx"


export default function DashBoardHeaderFilter() {
    const order = React.useRef()

    const manager = useSelector(state => state.Manager.manager)
    
    function orderClick() {
        order.current.classList.toggle("rotate-svg-90")
        order.current.classList.toggle("rotate-svg-270")
    }

    return(
        <div className="dashboard-header-filter">
                    <div><button className="dashboarg-header-filter-open db-b-i bg-input"><FilterSVG fill="white"/></button></div>
            <div className="dashboarg-header-filter-order db-b-i color-white" onClick={orderClick}>
                <div className="dashboarg-header-order-place">
                    <p className="color-white">сначала</p>
                    <p className="color-white">приглашенные</p>
                </div>
                <div className="dashboarg-header-arrowsvg rotate-svg-90" ref={order}><ArrowRightSVG fill="white"/></div>
            </div>
            <div className="dashboarg-header-filter-infobox db-b-i">
                <p>{manager.quotas}</p>
                <p>доступных квот</p>
            </div>
        </div>
    )
}