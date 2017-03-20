#include "plotzoomer.h"
#include <QMouseEvent>
#include <QApplication>
#include "qwt_scale_map.h"
#include "qwt_plot.h"

PlotZoomer::PlotZoomer(QWidget *canvas, bool doReplot):
    QwtPlotZoomer(canvas,doReplot),
    _mouse_pressed(false),
    _zoom_enabled(false)
{
    this->setTrackerMode(AlwaysOff);
}

void PlotZoomer::widgetMousePressEvent(QMouseEvent *me)
{
    _mouse_pressed = false;
    this->setTrackerMode(AlwaysOff);
    auto patterns = this->mousePattern();
    for (QwtEventPattern::MousePattern& pattern: patterns)
    {
        if( this->mouseMatch(pattern, me) ){
            _mouse_pressed = true;
            _initial_pos = me->pos();
        }
    }
    QwtPlotPicker::widgetMousePressEvent( me );
}

void PlotZoomer::widgetMouseMoveEvent(QMouseEvent *me)
{
    static QCursor zoom_cursor(QPixmap(":/icons/resources/zoom_in_32px.png"));

    if( _mouse_pressed )
    {
        QRect rect( me->pos(), _initial_pos );
        QRectF zoomRect = invTransform( rect.normalized() );

        if( zoomRect.width()  > minZoomSize().width() &&
            zoomRect.height() > minZoomSize().height()    )
        {
            if( !_zoom_enabled)
            {
                _zoom_enabled = true;
                this->setRubberBand( RectRubberBand );
                QApplication::setOverrideCursor(zoom_cursor);
            }
        }
        else if( _zoom_enabled)
        {
           _zoom_enabled = false;
           this->setRubberBand( NoRubberBand );
           QApplication::restoreOverrideCursor();
        }
    }
    QwtPlotPicker::widgetMouseMoveEvent( me );
}

void PlotZoomer::widgetMouseReleaseEvent(QMouseEvent *me)
{
    _mouse_pressed = false;
    _zoom_enabled = false;
    QApplication::restoreOverrideCursor();
    QwtPlotPicker::widgetMouseReleaseEvent( me );
}

bool PlotZoomer::accept(QPolygon &pa) const
{
    if ( pa.count() < 2 )
        return false;

    QRect rect = QRect( pa[0], pa[int( pa.count() ) - 1] );
    QRectF zoomRect = invTransform( rect.normalized() );

    if ( zoomRect.width()  < minZoomSize().width() &&
         zoomRect.height() < minZoomSize().height() ){
        return false;
    }
    return true;
}

QSizeF PlotZoomer::minZoomSize() const
{
    return QSizeF(scaleRect().width() * 0.02,
                  scaleRect().height() * 0.02);
}
