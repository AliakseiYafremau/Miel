import { createSlice } from "@reduxjs/toolkit"


const FilterSlice = createSlice({
    name: "filter",
    initialState: {
        filter: {
            min_age: "",
            max_age: "",
        },
        filterToggle: false
    },
    reducers: {
        setFilter(state, action) {
            state.filter = action.payload
        },
        setFilterToggle(state, action) {
            state.filterToggle = !state.filterToggle
        }
    }
});

export const { setFilter } = FilterSlice.actions;
export const { setFilterToggle } = FilterSlice.actions;

export default FilterSlice.reducer;