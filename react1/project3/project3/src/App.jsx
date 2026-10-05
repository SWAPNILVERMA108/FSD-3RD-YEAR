import React from 'react'
import Student2 from './components/Student2'

const App = () => {
  return (
    <div>
      <h1>My Student Records</h1>

      <div style={{ display: 'flex', gap: '20px' }}>

        <Student2
          name="Swapnil"
          section="27"
          image="https://beam-images.warnermediacdn.com/BEAM_LWM_DELIVERABLES/a500fccc-7dbe-45fb-91d4-023deb64bbc0/7cb449d5-f530-11ef-93b6-12953788022d?host=wbd-images.prod-vod.h264.io&partner=beamcom"
        />

        <Student2
          name="Rahul"
          section="28"
          image="./assets/image.png"
        />
p
        <Student2
          name="Aman"
          section="29"
          image=""
        />

      </div>
    </div>
  )
}

export default App