const $ = q => document.querySelector(q)
const AP = {} //Global shared storage
const _getProgressBar = type => $(`#main-modal > .attributes-holder > .attribute[type='${type}'] > .progress-bar > .val`)
const EL = {
    ZoneHolder: $('.zone-holder > .data'),
    AppTitle: $('#app-title'),
    modal: {
        name: $('#main-modal > .title'),
        food: _getProgressBar('Food'),
        water: _getProgressBar('Water'),
        capacityRatio: _getProgressBar('Capacity Ratio'),
        electricity: $(`#main-modal > .attributes-holder > .attribute[type='Electricity']`),
        distance: $(`#main-modal > .attributes-holder > .attribute[type='Distance to Threat'] > .val`),
        status: $(`#main-modal > .attributes-holder > .attribute[type='Status'] > .val`),
        // TODO: Link other dom elements here Broken WE NEED TO SPACE THEM OUT
    },
}
const getZoneHealth = zone => {
    const {food, water, electricity, occupancy, capacity} = zone
    const occupancyRatio = occupancy/capacity
    if (food < 25 || water < 25 || electricity.toLowerCase() == "no" || occupancyRatio > .98 || /urgent|must|desperate/ig.test(status)) return 'Bad'
    if (food < 50 || water < 50 || occupancyRatio > .85 || /like|at some point/ig.test(status)) return 'Fair'
    return 'Good'
}
const makeZoneHTML = (z,i) => {
    const zoneStatus = getZoneHealth(z) // Good, Fair, Bad
    const text = `
        <button class='zone ${zoneStatus.toLowerCase()}' onclick='openModal(${i})'>${z.name}</button>
    `.trim(/\s/)
    return text
}
const fetchEpicenter = _ => {
    fetch('/api/getEpicenter')
        .then(resp => resp.json())
        .then(epicenter => {
            AP.epicenter = epicenter
            console.log('Epicenter located at', epicenter)
        })
}
const fetchPageData = _ => {
    fetch('/api/listZones')
        .then(resp => resp.json())
        .then(zones => {
            AP.zones = zones = zones || []
            const zonesHTML = zones.map(makeZoneHTML).join("")
            EL.ZoneHolder.innerHTML = zonesHTML
        })
        .then(_ => {
            EL.AppTitle.setAttribute('last-updated', new Date().toLocaleString().split(', ')[1])
            !isNaN(AP.lastZone) && fillModalData(AP.zones[AP.lastZone])
        })
}
AP.fetchThread = setInterval(fetchPageData, 2e3)
fetchPageData()
fetchEpicenter()