import {renderOrb} from "@meya-ai/meya-orb"
import React from "react"

function main() {
    renderOrb({
        connectionOptions: {
            gridUrl: process.env.MEYA_GRID_URL as string,
            appId: process.env.APP_ID as string,
            integrationId: "integration.orb",
        },
        theme: {
            brandColor: "#1867d2",
            botAvatarUrl: "https://upload.wikimedia.org/wikipedia/commons/5/53/Google_%22G%22_Logo.svg",
            botAvatarMonogram: undefined,
        },
        container: document.getElementById("orb-mount"),
        windowFunctions: true,
    })
}

main()
