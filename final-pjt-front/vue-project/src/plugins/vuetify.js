import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import { VApp, VAppBar, VContainer, VSpacer, VBtn, VIcon, VToolbarTitle, VToolbarItems } from 'vuetify/components'

const vuetify = createVuetify({
  components: {
    VApp,
    VAppBar,
    VContainer,
    VSpacer,
    VBtn,
    VIcon,
    VToolbarTitle,
    VToolbarItems,
  },
  theme: {
    defaultTheme: 'light',
    themes: {
      light: {
        colors: {
          primary: '#339af0',
        },
      },
    },
  },
})

export default vuetify
