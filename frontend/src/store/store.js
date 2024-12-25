import { configureStore } from "@reduxjs/toolkit"

import FieldErrorSlice from "./slice/FieldErrorSlice"
import PageSlice from "./slice/pageSlice"
import HeaderToggleSlice from "./slice/HeaderToggleSlice"
import ManagerSlice from "./slice/ManagerSlice"
import FilterSlice from "./slice/FilterSlice"


export default configureStore({
    reducer: {
        FieldError: FieldErrorSlice,
        Page: PageSlice,
        HeaderToggle: HeaderToggleSlice,
        Manager: ManagerSlice,
        Filter: FilterSlice,
    }
})