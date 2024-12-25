import React from "react"
import { useDispatch, useSelector } from "react-redux"
import { useNavigate, useLocation } from "react-router"

import "./CandidateContainer.css"
import Star1SVG from "../SVG/Star1.jsx"
import Star2SVG from "../SVG/Star2.jsx"
import StickyNoteSVG from "../SVG/StickyNote.jsx"
import { setChangePage, setPreviousPage } from "../../store/slice/pageSlice.js"
import { declensionsQuantity } from "../../export/fun.js"


export default function CandidateContainer(props) {
    const now = new Date()

    const dispatch = useDispatch()
    const set_change = (obj) => dispatch(setChangePage(obj))
    const set_previous_page = (obj) => dispatch(setPreviousPage(obj))

    const manager = useSelector(state => state.Manager.manager)

    const navigate = useNavigate()
    const pathname = useLocation().pathname
    
    let candidate = ""
    let note = ""
    let favorite = ""

    if (pathname == "/home") {candidate = props.candidate} else {candidate = props.candidate.candidate}
    const candidate_fullname = candidate.full_name.split(" ", 3)
    const candidate_birth = new Date (candidate.date_of_birth)
    const candidate_age = Math.floor(new Date(now - candidate_birth) / (1000 * 60 * 60 * 24 * 365.25))
    const age_declensions = declensionsQuantity(candidate_age, ["год", "года", "лет"])
    const exp_declensions = declensionsQuantity(candidate.years_of_experience, ["год", "года", "лет"])

    manager.candidates.map((can) => {
        if (can.candidate_id == candidate.id) {
            note = can.note
            favorite = can.is_favorite
        }
    })
    
    function toCandidate() {
        pageTransitions(`/candidate?id=${candidate.id}`)
    }

    function pageTransitions(page) {
        set_previous_page(pathname)
        set_change(true)
        setTimeout(() => {
            navigate(page)
            set_change(false)
        }, 500)
    }

    React.useEffect(() => {
    }, [])

    return(
        <div className="сandidate">
            <div className="candidate-container" onClick={toCandidate}>
                <div className= { pathname == "/home" ? "candidate-photo" : "candidate-photo-extend"}>
                    <img src={`https://backend-y9b6.onrender.com/upload/photos/${candidate.photo}`} alt="" className=""/>
                </div>
                <div className="candidate-content">
                    <div className="candidate-title">
                        <div className="candidate-name bold">
                            <p>{candidate_fullname[0]}</p>
                            <p>{candidate_fullname[1]} {candidate_fullname[2]} {candidate.patronymic}</p>
                        </div>
                        { favorite ? <Star2SVG stroke="primary"/> : <Star1SVG stroke="primary"/>}
                    </div>
                    <div className="candidate-age">
                        {candidate_age} {age_declensions}
                    </div>
                    <div className="candidate-expinv">
                        <div className="candidate-exp">
                            {candidate.years_of_experience > 0 ? `Опыт:  ${candidate.years_of_experience} ${exp_declensions}` : "Без опыта"}
                        </div>
                        { pathname == "/home" ? 
                        <div className="candidate-inv">
                            {candidate.managers > 0 ? <p className="border-primary">приглашен</p> : <p className="border-secondary-1">cвободен</p>}
                        </div>
                        :
                        ""
                        }
                    </div>
                    { pathname == "/profile/history" ? 
                    <div className="candidate-history">
                        <p>был приглашён {new Date(props.candidate.created_at).toLocaleDateString('en-GB').replace(/\//g, ".")}</p>
                    </div> 
                    :
                    ""
                    }
                </div>
            </div>
            {note ? 
            <div className="candidate-note">
                <p>{note}</p>
                <div className="candidate-note-ico">
                    <StickyNoteSVG/><p>Заметка</p>
                </div>
            </div>
            : ""}
        </div>
    )
}