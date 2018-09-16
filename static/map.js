const genLatLong = z => ({lat: +z.lat, lng: +(z.long || z.lng)})
const lineSymbol = {
    path: 'M 0,-1 0,1',
    strokeOpacity: 1,
    scale: 4,
}
const icons = {
    home: `/static/home-icon.png`,
    hurricane: `/static/hurricane-icon.png`,
}
const makeMarker = (z,icon) => {
    const loc = genLatLong(z)
    new google.maps.Marker({
        position: loc,
        map: AP.map,
        icon: icons[icon=='hurricane'?'hurricane':'home'],
    })
    new google.maps.Polyline({
        position: [loc, AP.epicenter],
        icons: [{
            icon: lineSymbol,
            offset: '100%'
        }],
        map: AP.map,
    })
}

window.initMap = async _ => {
    console.log('Attempting to setup map')
    if (!AP.zones || !AP.epicenter) return setTimeout(window.initMap, 1000)
    console.log('Ok making MAP!')
    AP.map = new google.maps.Map(
        document.getElementById('map'), {zoom: 4, center: AP.epicenter})
    makeMarker(AP.epicenter, 'hurricane')
    AP.zones.forEach(makeMarker)
}

