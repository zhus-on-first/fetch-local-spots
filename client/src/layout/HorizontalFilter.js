import React from "react"
import { Link } from "react-router-dom"

import "../styles/HorizontalFilterStyles.css"

function HorizontalFilter() {
    return (
        <div className="horizontal-filter">
            <Link to="/locations/find-a-hike">Find a Hike</Link> |
            <Link to="/locations/find-a-food-spot">Find a Food Spot</Link> |
            <Link to="/locations/find-a-ride">Find a Ride</Link> |
            <Link to="/locations/5">Location 5 Details</Link> |
            <Link to="/locations//page/1">Catch All</Link> |
        </div>
    )
}

export default HorizontalFilter
