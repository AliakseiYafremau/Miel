import React from "react"
import { useDispatch, useSelector } from "react-redux"
import { useNavigate, useLocation } from "react-router"

import "./CandidateHeader.css"
import ArrowRightSVG from "../../SVG/ArrowRight.jsx"
import { declensionsQuantity } from "../../../export/fun.js"
import { setChangePage } from "../../../store/slice/pageSlice.js"
import { setCandidate } from "../../../store/slice/ManagerSlice.js"
import Star1SVG from "../../SVG/Star1.jsx"
import Star2SVG from "../../SVG/Star2.jsx"


export default function CandidateHeader() {
    const [favorite, setFavorite] = React.useState(false)

    const dispatch = useDispatch()
    const set_change = (obj) => dispatch(setChangePage(obj))
    const set_candidate = (obj) => dispatch(setCandidate(obj))

    const previous_page = useSelector(state => state.Page.previousPage)
    const candidate = useSelector(state => state.Manager.candidate)
    const candidates = useSelector(state => state.Manager.candidates)
    const manager = useSelector(state => state.Manager.manager)

    const navigate = useNavigate()
    const location = useLocation()
    const candidateID = new URLSearchParams(location.search).get("id")

    const candidate_age = new Date(candidate.date_of_birth).toLocaleDateString('en-GB').replace(/\//g, ".")
    const exp_declensions = declensionsQuantity(candidate.years_of_experience, ["год", "года", "лет"])

    function pageTransitions() {
        set_change(true)        
        setTimeout(() => {
            if (previous_page == 0){
                navigate("/home")
            } else {
                navigate(previous_page)
            }
            set_change(false)
        }, 500)
    }

    React.useEffect(() => {
        let ready = false
        if (candidates[0]){
            candidates.map(can => {
                if (can.id == candidateID) {                    
                    set_candidate(can)
                    ready = true
                }
            })
            if (!ready) {
                pageTransitions()
            }
        }
        manager.candidates.map((can) => {
            if (can.candidate_id == candidate.id) {
                setFavorite(can.is_favorite) 
            }
        })
    }, [])
    
    return(
        <div className="candidate-header">
            <div className="candidate-header-backfav">
                <div className="rotate-svg-180" onClick={pageTransitions}><ArrowRightSVG fill="white"/></div>
                { favorite ? <Star2SVG stroke="white"/> : <Star1SVG stroke="white"/> }
            </div>
            <div className="imgshadow"/>
            <div className="candidate-header-content">
                <div className="candidate-header-content-photocontainer">
                    <img src={`https://backend-y9b6.onrender.com/upload/photos/${candidate.photo}`} alt=""/>
                </div>
                <h4>{candidate.full_name}</h4>
                <div className="candidate-header-content-info">
                    <p>Дата рождения: {candidate_age}</p>
                    {candidate.years_of_experience > 0 ? <p>Опыт работы: {candidate.years_of_experience} {exp_declensions}</p> : <p>Без опыта</p>}
                </div>
            </div>
        </div>
    )
}