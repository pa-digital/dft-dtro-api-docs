(function () {
    "use strict";

    function initialiseTabset(tabset) {
        if (tabset.dataset.dtroTabsInitialised === "true") {
            return;
        }

        tabset.dataset.dtroTabsInitialised = "true";

        const tabs = Array.from(
            tabset.querySelectorAll(".dtro-tab")
        );

        const panels = Array.from(
            tabset.querySelectorAll(".dtro-tab-panel")
        );

        function selectTab(selectedTab) {
            const selectedPanelId =
                selectedTab.getAttribute("aria-controls");

            tabs.forEach(function (tab) {
                const selected =
                    tab === selectedTab;

                tab.classList.toggle(
                    "dtro-tab--active",
                    selected
                );

                tab.setAttribute(
                    "aria-selected",
                    selected ? "true" : "false"
                );

                tab.setAttribute(
                    "tabindex",
                    selected ? "0" : "-1"
                );
            });

            panels.forEach(function (panel) {
                const selected =
                    panel.id === selectedPanelId;

                panel.classList.toggle(
                    "dtro-tab-panel--active",
                    selected
                );
            });
        }

        tabs.forEach(function (tab, index) {
            tab.addEventListener("click", function () {
                selectTab(tab);
            });

            tab.addEventListener(
                "keydown",
                function (event) {
                    let nextIndex = index;

                    if (event.key === "ArrowRight") {
                        nextIndex =
                            (index + 1) % tabs.length;
                    } else if (
                        event.key === "ArrowLeft"
                    ) {
                        nextIndex =
                            (
                                index -
                                1 +
                                tabs.length
                            ) % tabs.length;
                    } else if (
                        event.key === "Home"
                    ) {
                        nextIndex = 0;
                    } else if (
                        event.key === "End"
                    ) {
                        nextIndex =
                            tabs.length - 1;
                    } else {
                        return;
                    }

                    event.preventDefault();

                    tabs[nextIndex].focus();
                    selectTab(tabs[nextIndex]);
                }
            );
        });

        const initiallySelected =
            tabs.find(function (tab) {
                return tab.classList.contains(
                    "dtro-tab--active"
                );
            }) || tabs[0];

        if (initiallySelected) {
            selectTab(initiallySelected);
        }
    }

    function initialiseTabs(root) {

        root
            .querySelectorAll(".dtro-tabset")
            .forEach(initialiseTabset);
    }

    function start() {

        console.log(
            "DTRO tabs script loaded"
        );

        initialiseTabs(document);

        const observer =
            new MutationObserver(function () {

                initialiseTabs(document);
            });

        observer.observe(document.body, {
            childList: true,
            subtree: true
        });
    }

    if (document.body) {
        start();
    } else {
        document.addEventListener(
            "DOMContentLoaded",
            start
        );
    }
})();